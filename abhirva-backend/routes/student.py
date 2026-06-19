from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from services.quiz_service import get_quiz_from_db, get_book_quiz_from_db, get_all_past_papers, get_past_paper_from_db
from config.supabase_client import supabase_db

router = APIRouter()

class SignupRequest(BaseModel):
    full_name: str
    email: Optional[str] = None
    role: Optional[str] = "STUDENT"
    grade: Optional[str] = None

@router.post("/signup")
async def signup(request: SignupRequest):
    """
    Creates a new student or parent profile.
    """
    try:
        response = supabase_db.table("profiles").insert({
            "full_name": request.full_name,
            "role": request.role.upper(),
            "free_tests_taken": 0,
            "total_points": 0,
            "grade": request.grade if request.role.upper() == "STUDENT" else None
        }).execute()
        
        if not response.data:
            raise Exception("Failed to create profile")
            
        student_id = response.data[0]["id"]
        return {"status": "success", "student_id": student_id, "full_name": request.full_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/past_papers")
async def fetch_past_papers():
    """
    Fetches all available past papers.
    """
    try:
        data = get_all_past_papers()
        if "error" in data:
            raise Exception(data["error"])
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/past_papers/start")
async def start_past_paper(request: PastPaperRequest):
    """
    Starts a past paper exam.
    """
    try:
        # Check student access (simplified for now, assume access)
        data = get_past_paper_from_db(request.past_paper_id)
        if "error" in data:
            raise HTTPException(status_code=404, detail=data["error"])
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class QuizRequest(BaseModel):
    student_id: str
    board: str
    grade: str
    subject: str
    chapter: str
    language: Optional[str] = "English"
    num_questions: Optional[int] = None

class PastPaperRequest(BaseModel):
    student_id: str
    past_paper_id: str

@router.post("/quiz/start")
async def start_quiz(request: QuizRequest):
    """
    Endpoint for a student to request a quiz.
    It will first check if the student has access, 
    then fetch the quiz from Supabase.
    """
    try:
        # Determine the required package name based on request parameters
        if request.board == "Library":
            package_name = "Book Library"
        elif request.subject in ["IMO Test", "NSO Test", "IEO Test", "SOF Test"] or request.board in ["IMO", "NSO", "IEO", "SOF"]:
            prefix = "IMO" if "IMO" in (request.subject or request.board) else (
                "NSO" if "NSO" in (request.subject or request.board) else (
                    "SOF" if "SOF" in (request.subject or request.board) else "IEO"
                )
            )
            package_name = f"{prefix} {request.grade}"
        else:
            # Map sub-subjects back to their master package
            sst_subs = ["History", "Geography", "Political Science", "Economics"]
            package_subject = "SST" if request.subject in sst_subs else request.subject
            package_name = f"{request.grade}th Board {package_subject} Booster"
            
        # First find the package ID by name
        pkg_resp = supabase_db.table("packages").select("id").ilike("name", f"%{package_name}%").execute()
        has_subscription = False
        
        if pkg_resp.data and len(pkg_resp.data) > 0:
            package_id = pkg_resp.data[0]["id"]
            # Check subscriptions
            sub_resp = supabase_db.table("subscriptions").select("id").eq("profile_id", request.student_id).eq("package_id", package_id).eq("status", "ACTIVE").execute()
            if sub_resp.data and len(sub_resp.data) > 0:
                has_subscription = True

        # If no subscription, check free_tests_taken
        if not has_subscription:
            profile_resp = supabase_db.table("profiles").select("free_tests_taken").eq("id", request.student_id).execute()
            
            if not profile_resp.data:
                raise HTTPException(status_code=404, detail="Student profile not found.")
                
            free_tests = profile_resp.data[0].get("free_tests_taken", 0)
            
            if free_tests >= 2:
                # Paywall hit
                raise HTTPException(
                    status_code=403, 
                    detail={"error": "TRIAL_EXHAUSTED", "message": f"You need the '{package_name}' package or your 2 free tests are exhausted. Please ask your parent to purchase this package."}
                )
            
            # Increment free_tests_taken
            new_count = free_tests + 1
            supabase_db.table("profiles").update({"free_tests_taken": new_count}).eq("id", request.student_id).execute()
            print(f"Student {request.student_id} consumed free test #{new_count} for {package_name}")
        else:
            print(f"Student {request.student_id} accessed quiz via active subscription to {package_name}.")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Access verification failed: {str(e)}")
    
    # Fetch quiz from DB
    if request.board == "Library":
        quiz_data = get_book_quiz_from_db(
            grade=request.grade,
            language=request.language,
            book_title=request.chapter
        )
    elif request.subject in ["IMO Test", "IMO", "NSO Test", "NSO", "IEO Test", "IEO", "SOF Test", "SOF"]:
        import random
        num_to_pick = request.num_questions if request.num_questions else 10
        
        # Fallback helper to query the correct tables
        use_olympiad_tables = True
        quiz_table = "olympiad_quizzes"
        question_table = "olympiad_questions"
        fk_field = "olympiad_quiz_id"
        
        # Test if olympiad_quizzes table exists, fallback to quizzes/questions if not
        try:
            supabase_db.table("olympiad_quizzes").select("id").limit(1).execute()
        except Exception:
            use_olympiad_tables = False
            quiz_table = "quizzes"
            question_table = "questions"
            fk_field = "quiz_id"

        if "mix" in request.chapter.lower():
            # Mix mode: get all quizzes for this grade and subject
            quizzes_resp = supabase_db.table(quiz_table).select("id").eq("grade", request.grade).eq("subject", request.subject).execute()
            if not quizzes_resp.data:
                raise HTTPException(status_code=404, detail=f"No {request.subject} quizzes have been published yet for {request.grade}. Please ask your administrator.")
            
            quiz_ids = [q["id"] for q in quizzes_resp.data]
            
            # Fetch all questions for these quiz IDs
            q_resp = supabase_db.table(question_table).select("*").in_(fk_field, quiz_ids).execute()
            if not q_resp.data:
                raise HTTPException(status_code=404, detail=f"No questions found for {request.subject} quizzes. Please check back later.")
                
            questions = q_resp.data
            random.shuffle(questions)
            selected_qs = questions[:num_to_pick]
            
            prefix_lower = "imo" if "IMO" in request.subject else (
                "nso" if "NSO" in request.subject else (
                    "sof" if "SOF" in request.subject else "ieo"
                )
            )
            quiz_data = {
                "quiz_id": f"{prefix_lower}-mix-quiz",
                "board": request.board,
                "grade": request.grade,
                "subject": request.subject,
                "chapter_or_topic": "Mix of all topics",
                "questions": selected_qs
            }
        else:
            # Topic-wise mode: get quiz by chapter
            quiz_resp = supabase_db.table(quiz_table).select("id, board, grade, subject, chapter_or_topic").eq("grade", request.grade).eq("subject", request.subject).eq("chapter_or_topic", request.chapter).execute()
            if not quiz_resp.data:
                raise HTTPException(status_code=404, detail=f"The quiz for topic '{request.chapter}' has not been published yet.")
                
            quiz_row = quiz_resp.data[0]
            q_resp = supabase_db.table(question_table).select("*").eq(fk_field, quiz_row["id"]).execute()
            if not q_resp.data:
                raise HTTPException(status_code=404, detail="No questions found for this topic.")
                
            questions = q_resp.data
            random.shuffle(questions)
            selected_qs = questions[:num_to_pick]
            
            quiz_data = {
                "quiz_id": quiz_row["id"],
                "board": quiz_row["board"],
                "grade": quiz_row["grade"],
                "subject": quiz_row["subject"],
                "chapter_or_topic": quiz_row["chapter_or_topic"],
                "questions": selected_qs
            }
    else:
        quiz_data = get_quiz_from_db(
            board=request.board,
            grade=request.grade,
            subject=request.subject,
            chapter=request.chapter
        )
    
    if quiz_data.get("success") is False or "error" in quiz_data:
        # Return 404 if not generated yet
        raise HTTPException(status_code=404, detail="This quiz hasn't been published yet. Please ask your administrator.")
        
    return {
        "status": "success",
        "message": "Quiz loaded successfully",
        "data": quiz_data
    }
