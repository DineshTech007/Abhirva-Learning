-- SQL Schema for Abhirva Learning Olympiad Prep (IMO, NSO, IEO)
-- You can run this in your Supabase SQL Editor to store Olympiad Quizzes in dedicated tables.

-- 1. Olympiad Quizzes Table (representing syllabus topics/sections)
CREATE TABLE olympiad_quizzes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    board VARCHAR(50) NOT NULL DEFAULT 'CBSE',
    grade VARCHAR(50) NOT NULL,
    subject VARCHAR(50) NOT NULL, -- 'IMO Test', 'NSO Test', 'IEO Test'
    chapter_or_topic VARCHAR(255) NOT NULL, -- e.g., 'Logical Reasoning', 'Science', etc.
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Unique constraint for grade + subject + topic
    UNIQUE(grade, subject, chapter_or_topic)
);

-- 2. Olympiad Questions Table
CREATE TABLE olympiad_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    olympiad_quiz_id UUID REFERENCES olympiad_quizzes(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) NOT NULL DEFAULT 'MCQ',
    difficulty_level VARCHAR(50) NOT NULL DEFAULT 'Medium', -- 'Easy', 'Medium', 'Hard'
    options JSONB NOT NULL, -- Array of strings
    correct_option TEXT NOT NULL,
    solution_steps TEXT,
    explanation_description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
