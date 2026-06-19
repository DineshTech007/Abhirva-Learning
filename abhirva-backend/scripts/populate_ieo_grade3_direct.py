import os
import sys

# Ensure the backend directory is in the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.supabase_client import supabase_db

def get_word_structure_knowledge():
    return [
        {
            "question_text": "Choose the correct spelling of the word that means a drawing or map of a town or building.",
            "options": ["Sketc", "Sketch", "Sketsh", "Skech"],
            "correct_option": "Sketch",
            "difficulty_level": "Easy",
            "solution_steps": "The correct spelling is S-K-E-T-C-H.",
            "explanation_description": "Spelling check."
        },
        {
            "question_text": "Choose the correct noun to fill in the blank: A ______ of bees flew over the garden.",
            "options": ["pack", "swarm", "flock", "herd"],
            "correct_option": "swarm",
            "difficulty_level": "Easy",
            "solution_steps": "The collective noun for bees is a 'swarm'.",
            "explanation_description": "Collective nouns."
        },
        {
            "question_text": "Fill in the blank with the correct pronoun: Sally and Rohit are siblings. ______ go to the same school.",
            "options": ["We", "She", "They", "He"],
            "correct_option": "They",
            "difficulty_level": "Easy",
            "solution_steps": "Since Sally and Rohit are plural third-person subjects, the pronoun 'They' is used.",
            "explanation_description": "Personal pronouns."
        },
        {
            "question_text": "Choose the correct adjective to fill in the blank: This puzzle is very ______; I cannot solve it.",
            "options": ["easy", "hard", "soft", "light"],
            "correct_option": "hard",
            "difficulty_level": "Easy",
            "solution_steps": "Since it cannot be solved, the puzzle is difficult or 'hard'.",
            "explanation_description": "Descriptive adjectives."
        },
        {
            "question_text": "Choose the correct verb form to fill in the blank: The sun ______ in the east every morning.",
            "options": ["rise", "rises", "rising", "rose"],
            "correct_option": "rises",
            "difficulty_level": "Easy",
            "solution_steps": "For singular third-person 'The sun' in simple present tense, the verb is 'rises'.",
            "explanation_description": "Subject-verb agreement."
        },
        {
            "question_text": "Choose the correct adverb to fill in the blank: The tortoise walked ______ and reached the finish line.",
            "options": ["quickly", "slowly", "loudly", "angrily"],
            "correct_option": "slowly",
            "difficulty_level": "Easy",
            "solution_steps": "Tortoises are known for moving slowly. So 'slowly' fits the context.",
            "explanation_description": "Adverbs of manner."
        },
        {
            "question_text": "Fill in the blank with the correct preposition: The cat is sleeping ______ the table.",
            "options": ["under", "between", "through", "during"],
            "correct_option": "under",
            "difficulty_level": "Easy",
            "solution_steps": "Sleeping under a table is a standard spatial relationship.",
            "explanation_description": "Prepositions of place."
        },
        {
            "question_text": "Choose the correct article to fill in the blank: I saw ______ owl sitting on a tree branch.",
            "options": ["a", "an", "the", "no article"],
            "correct_option": "an",
            "difficulty_level": "Easy",
            "solution_steps": "'Owl' starts with a vowel sound, so 'an' is used.",
            "explanation_description": "Indefinite articles."
        },
        {
            "question_text": "Choose the correct conjunction to fill in the blank: I wanted to play outside, ______ it was raining heavily.",
            "options": ["so", "or", "but", "because"],
            "correct_option": "but",
            "difficulty_level": "Easy",
            "solution_steps": "'but' is used to show contrast between wanting to play and the rain.",
            "explanation_description": "Coordinating conjunctions."
        },
        {
            "question_text": "What is the synonym of the word 'large'?",
            "options": ["Huge", "Tiny", "Short", "Small"],
            "correct_option": "Huge",
            "difficulty_level": "Easy",
            "solution_steps": "Huge has the same meaning as large.",
            "explanation_description": "Synonyms."
        },
        {
            "question_text": "What is the antonym of the word 'happy'?",
            "options": ["Glad", "Cheerful", "Sad", "Jolly"],
            "correct_option": "Sad",
            "difficulty_level": "Easy",
            "solution_steps": "Sad is the opposite of happy.",
            "explanation_description": "Antonyms."
        },
        {
            "question_text": "What is the plural form of the word 'child'?",
            "options": ["Childs", "Children", "Childrens", "Childes"],
            "correct_option": "Children",
            "difficulty_level": "Easy",
            "solution_steps": "'Child' has an irregular plural form, which is 'children'.",
            "explanation_description": "Irregular plurals."
        },
        {
            "question_text": "Choose the correct option: A person who cures sick people is a ______.",
            "options": ["Teacher", "Doctor", "Driver", "Farmer"],
            "correct_option": "Doctor",
            "difficulty_level": "Easy",
            "solution_steps": "A doctor is a professional who treats patients.",
            "explanation_description": "Occupations/Vocabulary."
        },
        {
            "question_text": "Fill in the blank with the correct tense: Yesterday, my father ______ a new bicycle for me.",
            "options": ["buy", "buys", "bought", "buying"],
            "correct_option": "bought",
            "difficulty_level": "Medium",
            "solution_steps": "'Yesterday' indicates the past tense. The past tense of buy is 'bought'.",
            "explanation_description": "Simple past tense."
        },
        {
            "question_text": "Choose the correct homophone: Can you ______ the sound of the birds?",
            "options": ["here", "hear", "hare", "hair"],
            "correct_option": "hear",
            "difficulty_level": "Medium",
            "solution_steps": "'Hear' refers to listening/perceiving sound. 'Here' refers to a place.",
            "explanation_description": "Homophones."
        },
        {
            "question_text": "Choose the feminine gender of the word 'King'.",
            "options": ["Princess", "Queen", "Empress", "Duchess"],
            "correct_option": "Queen",
            "difficulty_level": "Easy",
            "solution_steps": "The feminine equivalent of King is Queen.",
            "explanation_description": "Gender nouns."
        },
        {
            "question_text": "Choose the correct option: Which of these is a household item used for sweeping?",
            "options": ["Broom", "Spoon", "Knife", "Bucket"],
            "correct_option": "Broom",
            "difficulty_level": "Easy",
            "solution_steps": "A broom is used for cleaning/sweeping floors.",
            "explanation_description": "Household items vocabulary."
        },
        {
            "question_text": "Choose the correct spelling of the word that means the opposite of simple.",
            "options": ["Complicatd", "Complicated", "Complecated", "Complycated"],
            "correct_option": "Complicated",
            "difficulty_level": "Medium",
            "solution_steps": "The correct spelling is C-O-M-P-L-I-C-A-T-E-D.",
            "explanation_description": "Spelling check."
        },
        {
            "question_text": "Choose the correct preposition: The book is ______ the bag.",
            "options": ["inside", "over", "between", "through"],
            "correct_option": "inside",
            "difficulty_level": "Easy",
            "solution_steps": "Books are kept inside a bag.",
            "explanation_description": "Preposition."
        },
        {
            "question_text": "Find the noun in the sentence: 'The small dog barked loudly.'",
            "options": ["small", "dog", "barked", "loudly"],
            "correct_option": "dog",
            "difficulty_level": "Easy",
            "solution_steps": "'dog' is the name of an animal, hence it is a noun.",
            "explanation_description": "Parts of speech."
        },
        {
            "question_text": "Find the verb in the sentence: 'She writes a letter.'",
            "options": ["She", "writes", "letter", "a"],
            "correct_option": "writes",
            "difficulty_level": "Easy",
            "solution_steps": "'writes' is the action word in the sentence.",
            "explanation_description": "Verbs."
        },
        {
            "question_text": "Choose the correct antonym of 'brave'.",
            "options": ["Cowardly", "Strong", "Fearless", "Heroic"],
            "correct_option": "Cowardly",
            "difficulty_level": "Medium",
            "solution_steps": "Cowardly is the opposite of brave.",
            "explanation_description": "Antonyms."
        },
        {
            "question_text": "What is the singular form of 'knives'?",
            "options": ["Knif", "Knife", "Knive", "Knifes"],
            "correct_option": "Knife",
            "difficulty_level": "Medium",
            "solution_steps": "Nouns ending in 'fe' change to 'ves' in plural. So singular is 'knife'.",
            "explanation_description": "Singular-plural."
        },
        {
            "question_text": "Complete the phrase: 'As cold as ______.'",
            "options": ["coal", "ice", "water", "stone"],
            "correct_option": "ice",
            "difficulty_level": "Easy",
            "solution_steps": "The standard simile is 'As cold as ice'.",
            "explanation_description": "Similes/Phrases."
        },
        {
            "question_text": "Choose the correct article: He is ______ honest boy.",
            "options": ["a", "an", "the", "no article"],
            "correct_option": "an",
            "difficulty_level": "Medium",
            "solution_steps": "'Honest' starts with a silent 'h' and a vowel sound 'o', so it takes 'an'.",
            "explanation_description": "Articles."
        },
        {
            "question_text": "Unscramble the letters to make a meaningful word: 'E T C A R E H'",
            "options": ["TEACHER", "REACHER", "CREATE", "CHEATER"],
            "correct_option": "TEACHER",
            "difficulty_level": "Medium",
            "solution_steps": "Rearranging the letters E, T, C, A, R, E, H gives TEACHER.",
            "explanation_description": "Jumbled words."
        },
        {
            "question_text": "Choose the correct word: Which animal makes a 'neigh' sound?",
            "options": ["Lion", "Dog", "Horse", "Sheep"],
            "correct_option": "Horse",
            "difficulty_level": "Easy",
            "solution_steps": "Horses neigh, lions roar, dogs bark, sheep bleat.",
            "explanation_description": "Animal sounds."
        },
        {
            "question_text": "Choose the correct option to fill in the blank: We ______ tennis every Saturday.",
            "options": ["plays", "play", "playing", "played"],
            "correct_option": "play",
            "difficulty_level": "Easy",
            "solution_steps": "For first person plural 'We', simple present verb is 'play'.",
            "explanation_description": "Tenses."
        },
        {
            "question_text": "Identify the conjunction: 'He failed because he did not study.'",
            "options": ["He", "failed", "because", "study"],
            "correct_option": "because",
            "difficulty_level": "Easy",
            "solution_steps": "'because' connects two clauses, making it a conjunction.",
            "explanation_description": "Conjunctions."
        },
        {
            "question_text": "Choose the correct pronoun: 'This is Rohit's book. Give it to ______.'",
            "options": ["him", "his", "he", "her"],
            "correct_option": "him",
            "difficulty_level": "Easy",
            "solution_steps": "Rohit is male, so object pronoun is 'him'.",
            "explanation_description": "Pronouns."
        },
        {
            "question_text": "Choose the correct synonym of 'beautiful'.",
            "options": ["Pretty", "Ugly", "Dirty", "Rough"],
            "correct_option": "Pretty",
            "difficulty_level": "Easy",
            "solution_steps": "Pretty has a similar meaning to beautiful.",
            "explanation_description": "Synonyms."
        },
        {
            "question_text": "Identify the type of sentence: 'Please shut the door.'",
            "options": ["Statement", "Question", "Request/Command", "Exclamation"],
            "correct_option": "Request/Command",
            "difficulty_level": "Medium",
            "solution_steps": "Sentences starting with 'Please' are requests.",
            "explanation_description": "Sentence types."
        },
        {
            "question_text": "Choose the correct spelling:",
            "options": ["Tomorow", "Tomorrow", "Toomorrow", "Tomoroww"],
            "correct_option": "Tomorrow",
            "difficulty_level": "Easy",
            "solution_steps": "The correct spelling is T-O-M-O-R-R-O-W.",
            "explanation_description": "Spellings."
        },
        {
            "question_text": "Which of these is a fruit?",
            "options": ["Potato", "Onion", "Apple", "Carrot"],
            "correct_option": "Apple",
            "difficulty_level": "Easy",
            "solution_steps": "Apple is a sweet fruit. Potatoes and onions are vegetables.",
            "explanation_description": "Basic categories."
        },
        {
            "question_text": "Choose the correct homophone: The wind ______ the leaves away.",
            "options": ["blue", "blew", "blow", "blown"],
            "correct_option": "blew",
            "difficulty_level": "Medium",
            "solution_steps": "'Blew' is the past tense of blow. 'Blue' is a color.",
            "explanation_description": "Homophones."
        },
        {
            "question_text": "Choose the correct preposition: We are going to school ______ bus.",
            "options": ["on", "by", "with", "in"],
            "correct_option": "by",
            "difficulty_level": "Easy",
            "solution_steps": "The preposition used for modes of transport is 'by' (by bus, by car).",
            "explanation_description": "Prepositions."
        },
        {
            "question_text": "What is the feminine gender of 'Uncle'?",
            "options": ["Aunt", "Niece", "Mother", "Sister"],
            "correct_option": "Aunt",
            "difficulty_level": "Easy",
            "solution_steps": "The feminine equivalent of Uncle is Aunt.",
            "explanation_description": "Gender terms."
        },
        {
            "question_text": "Choose the correct punctuation mark for: 'Wow, what a beautiful drawing'",
            "options": ["Period (.)", "Exclamation mark (!)", "Question mark (?)", "Comma (,)"],
            "correct_option": "Exclamation mark (!)",
            "difficulty_level": "Easy",
            "solution_steps": "'Wow' shows strong emotion, requiring an exclamation mark.",
            "explanation_description": "Punctuation."
        },
        {
            "question_text": "Choose the correct adjective: An elephant is a ______ animal.",
            "options": ["tiny", "huge", "small", "thin"],
            "correct_option": "huge",
            "difficulty_level": "Easy",
            "solution_steps": "Elephants are large/huge.",
            "explanation_description": "Adjectives."
        },
        {
            "question_text": "Choose the correct singular form of 'flies'.",
            "options": ["Fly", "Flie", "Fli", "Flyes"],
            "correct_option": "Fly",
            "difficulty_level": "Medium",
            "solution_steps": "Nouns ending in 'y' preceded by consonant change to 'ies'. So singular is 'fly'.",
            "explanation_description": "Singular-plural."
        }
    ]

def get_reading():
    return [
        {
            "question_text": "Read the short text and answer: 'You are invited to Rohan's 9th birthday party at his house on Sunday at 4 p.m.' What is the event?",
            "options": ["School picnic", "Birthday party", "Wedding", "Festival celebration"],
            "correct_option": "Birthday party",
            "difficulty_level": "Easy",
            "solution_steps": "The text states 'You are invited to Rohan's 9th birthday party'.",
            "explanation_description": "Comprehension - invitation."
        },
        {
            "question_text": "Read the text and answer: 'The library is open from 9 a.m. to 5 p.m. on weekdays and 10 a.m. to 2 p.m. on Saturdays.' When does the library close on Saturdays?",
            "options": ["5 p.m.", "9 a.m.", "2 p.m.", "10 a.m."],
            "correct_option": "2 p.m.",
            "difficulty_level": "Medium",
            "solution_steps": "The text says '10 a.m. to 2 p.m. on Saturdays'. So it closes at 2 p.m.",
            "explanation_description": "Comprehension - timetables."
        },
        {
            "question_text": "Read the passage: 'A thirsty crow found a pitcher with a little water at the bottom. He could not reach it. He dropped small pebbles into the pitcher until the water rose to the top.' How did the crow solve his problem?",
            "options": ["He broke the pitcher", "He flew away", "He dropped pebbles inside", "He drank from a lake"],
            "correct_option": "He dropped pebbles inside",
            "difficulty_level": "Easy",
            "solution_steps": "The text says 'He dropped small pebbles into the pitcher until the water rose'.",
            "explanation_description": "Comprehension - story details."
        },
        {
            "question_text": "From the crow story, what can we say about the crow?",
            "options": ["He was lazy", "He was clever", "He was foolish", "He was angry"],
            "correct_option": "He was clever",
            "difficulty_level": "Easy",
            "solution_steps": "Solving a problem with a smart idea shows he was clever.",
            "explanation_description": "Comprehension - inference."
        },
        {
            "question_text": "Read the notice: 'All students must wear clean white uniforms for the assembly on Monday. Principal.' Who wrote this notice?",
            "options": ["A student", "The teacher", "The Principal", "A parent"],
            "correct_option": "The Principal",
            "difficulty_level": "Easy",
            "solution_steps": "The notice is signed by 'Principal'.",
            "explanation_description": "Comprehension - notice."
        },
        {
            "question_text": "From the Principal's notice, when should students wear white uniforms?",
            "options": ["Every day", "On Sunday", "On Monday", "On Saturday"],
            "correct_option": "On Monday",
            "difficulty_level": "Easy",
            "solution_steps": "The notice states 'for the assembly on Monday'.",
            "explanation_description": "Comprehension - specific info."
        },
        {
            "question_text": "Read the recipe step: 'First, wash the apples. Second, peel and slice them. Third, blend them with milk.' What is the second step?",
            "options": ["Wash the apples", "Blend with milk", "Peel and slice the apples", "Eat the apples"],
            "correct_option": "Peel and slice the apples",
            "difficulty_level": "Medium",
            "solution_steps": "The text states 'Second, peel and slice them'.",
            "explanation_description": "Comprehension - sequences."
        },
        {
            "question_text": "Read: 'Dear Uncle, thank you for the wonderful watch you sent me for my birthday. I love it! Love, Amit.' What did Uncle gift Amit?",
            "options": ["A book", "A toy car", "A watch", "A shirt"],
            "correct_option": "A watch",
            "difficulty_level": "Easy",
            "solution_steps": "Amit writes 'thank you for the wonderful watch you sent me'.",
            "explanation_description": "Comprehension - thank you note."
        },
        {
            "question_text": "Why did Amit write a letter to his Uncle?",
            "options": ["To ask for money", "To invite him to a party", "To thank him for a gift", "To complain about a watch"],
            "correct_option": "To thank him for a gift",
            "difficulty_level": "Medium",
            "solution_steps": "Amit starts with 'thank you for the wonderful watch'.",
            "explanation_description": "Comprehension - purpose."
        },
        {
            "question_text": "Read the timetable: 'Flight AI-101 to Mumbai is delayed. New departure time is 6:45 p.m. instead of 5:15 p.m.' By how much time is the flight delayed?",
            "options": ["1 hour", "1 hour 30 minutes", "2 hours", "45 minutes"],
            "correct_option": "1 hour 30 minutes",
            "difficulty_level": "Hard",
            "solution_steps": "From 5:15 p.m. to 6:45 p.m. is exactly 1 hour and 30 minutes.",
            "explanation_description": "Comprehension - timetable math."
        },
        {
            "question_text": "Read the story: 'Rani has a pet dog named Sparky. He has brown fur and loves to fetch tennis balls. Every evening, Rani takes him to the park.' What color is Sparky's fur?",
            "options": ["Black", "Brown", "White", "Golden"],
            "correct_option": "Brown",
            "difficulty_level": "Easy",
            "solution_steps": "The text says 'He has brown fur'.",
            "explanation_description": "Comprehension - details."
        },
        {
            "question_text": "From the Rani story, what does Sparky love to do?",
            "options": ["Chase cats", "Bark at cars", "Fetch tennis balls", "Sleep all day"],
            "correct_option": "Fetch tennis balls",
            "difficulty_level": "Easy",
            "solution_steps": "The text says 'loves to fetch tennis balls'.",
            "explanation_description": "Comprehension - preferences."
        },
        {
            "question_text": "Read the dialogue: 'Mother: Don't forget your umbrella, Rohan. It's cloudy outside. Rohan: Okay, Mom!' What is the weather like?",
            "options": ["Sunny", "Rainy/Cloudy", "Snowing", "Windy"],
            "correct_option": "Rainy/Cloudy",
            "difficulty_level": "Easy",
            "solution_steps": "Mother says 'It's cloudy outside' and suggests carrying an umbrella.",
            "explanation_description": "Comprehension - inference."
        },
        {
            "question_text": "Read: 'Lost! A blue pencil case containing three gel pens and a ruler. If found, please return to Grade 3-A classroom.' What is lost?",
            "options": ["Gel pens", "A ruler", "A blue pencil case", "A textbook"],
            "correct_option": "A blue pencil case",
            "difficulty_level": "Easy",
            "solution_steps": "The lost announcement starts with 'Lost! A blue pencil case'.",
            "explanation_description": "Comprehension - lost notice."
        },
        {
            "question_text": "Where should the finder return the lost pencil case?",
            "options": ["To the staffroom", "To the library", "To Grade 3-A classroom", "To the office"],
            "correct_option": "To Grade 3-A classroom",
            "difficulty_level": "Easy",
            "solution_steps": "The notice says 'please return to Grade 3-A classroom'.",
            "explanation_description": "Comprehension - instructions."
        },
        {
            "question_text": "Read: 'School Bus Route A will not run tomorrow due to road repairs. Parents are requested to make self-travel arrangements.' Why will the bus not run?",
            "options": ["Bus is broken", "Driver is sick", "Road repairs", "Bad weather"],
            "correct_option": "Road repairs",
            "difficulty_level": "Medium",
            "solution_steps": "The text mentions 'due to road repairs'.",
            "explanation_description": "Comprehension - cause."
        },
        {
            "question_text": "Read the anecdote: 'A little girl asked her grandmother how old she was. Grandmother smiled and said, \"I am as old as my tongue and a little older than my teeth!\"' What did Grandmother do when asked her age?",
            "options": ["She got angry", "She cried", "She gave a playful, funny answer", "She told her exact age"],
            "correct_option": "She gave a playful, funny answer",
            "difficulty_level": "Hard",
            "solution_steps": "Saying 'older than my teeth' is a classic riddle/playful response.",
            "explanation_description": "Comprehension - tone."
        },
        {
            "question_text": "Read: 'Please join us for a housewarming party at our new home, Villa-45, Green Meadows, on Friday at 6:30 p.m. RSVP by Wednesday.' By which day must you reply?",
            "options": ["Friday", "Wednesday", "Thursday", "Saturday"],
            "correct_option": "Wednesday",
            "difficulty_level": "Medium",
            "solution_steps": "RSVP means please reply. The card says 'RSVP by Wednesday'.",
            "explanation_description": "Comprehension - abbreviations."
        },
        {
            "question_text": "Read: 'The zoo has feeding times: Penguins at 11:00 a.m., Lions at 1:30 p.m., and Monkeys at 3:00 p.m.' When can you watch the monkeys being fed?",
            "options": ["11:00 a.m.", "1:30 p.m.", "3:00 p.m.", "12:00 noon"],
            "correct_option": "3:00 p.m.",
            "difficulty_level": "Easy",
            "solution_steps": "The schedule states 'Monkeys at 3:00 p.m.'",
            "explanation_description": "Comprehension - lists."
        },
        {
            "question_text": "Read: 'Rahul went to buy fruit. Bananas were $2 a dozen, and apples were $4 a kg. He bought two dozen bananas.' How much did he spend?",
            "options": ["$2", "$4", "$6", "$8"],
            "correct_option": "$4",
            "difficulty_level": "Hard",
            "solution_steps": "1 dozen bananas = $2. He bought 2 dozen, so 2 * $2 = $4.",
            "explanation_description": "Comprehension - word math."
        }
    ]

def get_spoken_written_expression():
    return [
        {
            "question_text": "Choose the correct phrase to complete the conversation:\nTeacher: Class, quiet down please.\nStudents: ____________, Teacher.",
            "options": ["Thank you", "Sorry", "Welcome", "Excuse me"],
            "correct_option": "Sorry",
            "difficulty_level": "Easy",
            "solution_steps": "Apologizing for making noise is the correct response. So 'Sorry' is appropriate.",
            "explanation_description": "Classroom expressions."
        },
        {
            "question_text": "Complete the dialogue:\nFriend 1: I won the first prize in the drawing competition!\nFriend 2: ____________! I am so happy for you.",
            "options": ["Congratulations", "Happy Birthday", "Get well soon", "Happy journey"],
            "correct_option": "Congratulations",
            "difficulty_level": "Easy",
            "solution_steps": "We congratulate people on achievements.",
            "explanation_description": "Social greetings."
        },
        {
            "question_text": "Complete the conversation:\nCustomer: Excuse me, how much is this notebook?\nShopkeeper: ____________.",
            "options": ["It is blue", "It is 20 cents", "I have one", "Yes, please"],
            "correct_option": "It is 20 cents",
            "difficulty_level": "Easy",
            "solution_steps": "'How much' asks for the price. 'It is 20 cents' answers with a price.",
            "explanation_description": "Shopping interactions."
        },
        {
            "question_text": "Choose the best response:\nRohit: Would you like some cake?\nMeera: ____________. I am full.",
            "options": ["Yes, please", "No, thank you", "Sure", "Congratulations"],
            "correct_option": "No, thank you",
            "difficulty_level": "Easy",
            "solution_steps": "Since Meera is full, she declines politely with 'No, thank you'.",
            "explanation_description": "Polite refusals."
        },
        {
            "question_text": "Complete the conversation:\nFather: You did a great job cleaning your room!\nSon: ____________, Dad.",
            "options": ["Sorry", "Thank you", "Please", "Excuse me"],
            "correct_option": "Thank you",
            "difficulty_level": "Easy",
            "solution_steps": "The son thanks his father for the praise.",
            "explanation_description": "Expressing gratitude."
        },
        {
            "question_text": "Choose the best greeting when meeting someone for the first time in the morning:",
            "options": ["Good night", "Good morning", "Goodbye", "See you later"],
            "correct_option": "Good morning",
            "difficulty_level": "Easy",
            "solution_steps": "'Good morning' is the standard morning greeting.",
            "explanation_description": "Greetings."
        },
        {
            "question_text": "Complete the dialogue:\nStudent: May I go to the restroom, please?\nTeacher: ____________. Come back quickly.",
            "options": ["No, you don't", "Yes, you may", "Sorry", "Thank you"],
            "correct_option": "Yes, you may",
            "difficulty_level": "Easy",
            "solution_steps": "The teacher grants permission with 'Yes, you may'.",
            "explanation_description": "Permissions."
        },
        {
            "question_text": "Choose the correct phrase: If you accidentally step on someone's foot, you should say, '____________.'",
            "options": ["I am sorry", "Thank you", "Excuse me", "Welcome"],
            "correct_option": "I am sorry",
            "difficulty_level": "Easy",
            "solution_steps": "Apologize for an accidental bump with 'I am sorry'.",
            "explanation_description": "Apologies."
        },
        {
            "question_text": "Complete the dialogue:\nMother: It's bedtime now. Good night!\nChild: ____________, Mom!",
            "options": ["Good afternoon", "Good night", "Goodbye", "Hello"],
            "correct_option": "Good night",
            "difficulty_level": "Easy",
            "solution_steps": "The child responds to 'Good night' with 'Good night'.",
            "explanation_description": "Night routines."
        },
        {
            "question_text": "Choose the correct idiom meaning: 'A piece of cake' means ______.",
            "options": ["Very easy", "Very tasty", "Very hard", "A large portion"],
            "correct_option": "Very easy",
            "difficulty_level": "Medium",
            "solution_steps": "The idiom 'a piece of cake' is used to describe something very easy.",
            "explanation_description": "Idioms."
        },
        {
            "question_text": "Choose the correct proverb: 'Practice makes ______.'",
            "options": ["perfect", "better", "easy", "well"],
            "correct_option": "perfect",
            "difficulty_level": "Medium",
            "solution_steps": "The standard proverb is 'Practice makes perfect'.",
            "explanation_description": "Proverbs."
        },
        {
            "question_text": "Complete the conversation:\nVisitor: Can you show me the way to the library?\nGuide: Sure, ____________ and turn left.",
            "options": ["go straight", "turn back", "stop here", "sit down"],
            "correct_option": "go straight",
            "difficulty_level": "Medium",
            "solution_steps": "'Go straight' is a common directional instruction.",
            "explanation_description": "Giving directions."
        },
        {
            "question_text": "Choose the best response:\nAnil: Can I borrow your pencil?\nSunil: Sure, ____________.",
            "options": ["here you go", "sorry", "no way", "thank you"],
            "correct_option": "here you go",
            "difficulty_level": "Easy",
            "solution_steps": "When handing something to someone, we say 'here you go' or 'here it is'.",
            "explanation_description": "Sharing conversations."
        },
        {
            "question_text": "Complete the dialogue:\nDoctor: How do you feel today?\nPatient: I feel much ____________. Thank you, doctor.",
            "options": ["worse", "better", "sick", "bad"],
            "correct_option": "better",
            "difficulty_level": "Easy",
            "solution_steps": "Saying 'better' and thanking indicates recovery.",
            "explanation_description": "Health queries."
        },
        {
            "question_text": "Choose the correct phrase: If you want to ask a question in a crowded room, you say, '____________.'",
            "options": ["Sorry", "Excuse me", "Hello", "Pardon"],
            "correct_option": "Excuse me",
            "difficulty_level": "Medium",
            "solution_steps": "'Excuse me' is used to politely get attention in public or crowded situations.",
            "explanation_description": "Social politeness."
        },
        {
            "question_text": "Complete the dialogue:\nFriend 1: Have a safe trip!\nFriend 2: Thank you! ____________.",
            "options": ["Goodbye", "Welcome", "Nice to meet you", "Sorry"],
            "correct_option": "Goodbye",
            "difficulty_level": "Easy",
            "solution_steps": "When leaving for a trip, we say 'Goodbye' or 'Bye'.",
            "explanation_description": "Partings."
        },
        {
            "question_text": "Choose the correct response:\nTeacher: You have improved your handwriting a lot!\nStudent: ____________.",
            "options": ["I am sorry", "Thank you, Teacher", "Excuse me", "You are welcome"],
            "correct_option": "Thank you, Teacher",
            "difficulty_level": "Easy",
            "solution_steps": "Acknowledge praise from a teacher with gratitude.",
            "explanation_description": "Gratitude responses."
        },
        {
            "question_text": "Complete the conversation:\nHost: Welcome to our house!\nGuest: Thank you for ____________ me.",
            "options": ["inviting", "ignoring", "sending", "driving"],
            "correct_option": "inviting",
            "difficulty_level": "Medium",
            "solution_steps": "Guests thank hosts for inviting them.",
            "explanation_description": "Host-guest interactions."
        },
        {
            "question_text": "Choose the best response:\nMeera: I am sorry I broke your crayon.\nAnu: ____________. We can share mine.",
            "options": ["That is bad", "That is okay", "Don't touch it", "Sorry"],
            "correct_option": "That is okay",
            "difficulty_level": "Easy",
            "solution_steps": "Accepting an apology politely with 'That is okay' or 'No problem'.",
            "explanation_description": "Accepting apologies."
        },
        {
            "question_text": "Complete the dialogue:\nGrandma: Can you help me find my glasses?\nGrandchild: Sure, Grandma! ____________.",
            "options": ["I will search them", "I will look for them", "I am busy", "Sorry"],
            "correct_option": "I will look for them",
            "difficulty_level": "Medium",
            "solution_steps": "The phrasal verb meaning to search/find is 'look for'.",
            "explanation_description": "Phrasal verbs in speech."
        }
    ]

def get_achievers_section():
    return [
        {
            "question_text": "Choose the correct option to fill in the blank:\nRohit had to be ______ to the city hospital after his injury.",
            "options": ["sheltered", "located", "admitted", "placed"],
            "correct_option": "admitted",
            "difficulty_level": "Hard",
            "solution_steps": "When someone is kept in a hospital for treatment, they are 'admitted' to the hospital.",
            "explanation_description": "Verb usage in context."
        },
        {
            "question_text": "Choose the correct antonym of 'fallible' (which means capable of making mistakes).",
            "options": ["Imperfect", "Perfect", "Faulty", "Mistaken"],
            "correct_option": "Perfect",
            "difficulty_level": "Hard",
            "solution_steps": "Fallible means error-prone. The antonym is flawless or 'perfect'.",
            "explanation_description": "Hard antonyms."
        },
        {
            "question_text": "Choose the sentence that is grammatically correct.",
            "options": ["The candies were distributed between all the students.", "The candies were distributed among all the students.", "The candies distributed between students.", "The candies were distribute among all the students."],
            "correct_option": "The candies were distributed among all the students.",
            "difficulty_level": "Hard",
            "solution_steps": "'Between' is used for two people. For more than two (all the students), 'among' is correct.",
            "explanation_description": "Preposition error correction."
        },
        {
            "question_text": "Choose the correct option: Which word means 'a collection of books kept for reading or borrowing'?",
            "options": ["Classroom", "Laboratory", "Library", "Office"],
            "correct_option": "Library",
            "difficulty_level": "Medium",
            "solution_steps": "A library is a place containing books for public or private use.",
            "explanation_description": "One-word substitution."
        },
        {
            "question_text": "Choose the correct conjunction to join the sentences:\nHe was very tired. He finished his homework before sleeping.",
            "options": ["Although he was very tired, he finished his homework.", "He finished his homework because he was tired.", "He was tired so he finished his homework.", "Since he finished his homework, he was tired."],
            "correct_option": "Although he was very tired, he finished his homework.",
            "difficulty_level": "Hard",
            "solution_steps": "'Although' shows contrast, showing that he did the work despite his tiredness.",
            "explanation_description": "Conjunction synthesis."
        },
        {
            "question_text": "Choose the correct spelling of the word that means a pleasant sound/tune.",
            "options": ["Melody", "Mellody", "Melodye", "Milody"],
            "correct_option": "Melody",
            "difficulty_level": "Medium",
            "solution_steps": "The correct spelling is M-E-L-O-D-Y.",
            "explanation_description": "Spellings."
        },
        {
            "question_text": "Complete the proverb: 'Actions speak louder than ______.'",
            "options": ["mouths", "words", "speech", "sounds"],
            "correct_option": "words",
            "difficulty_level": "Medium",
            "solution_steps": "The proverb is 'Actions speak louder than words'.",
            "explanation_description": "Proverbs."
        },
        {
            "question_text": "Choose the correct pronoun: 'The cat licked ______ paws after drinking milk.'",
            "options": ["it's", "its", "her", "his"],
            "correct_option": "its",
            "difficulty_level": "Hard",
            "solution_steps": "'Its' is the possessive pronoun for animals. 'It's' is a contraction of 'it is'.",
            "explanation_description": "Possessive pronouns vs contractions."
        },
        {
            "question_text": "Choose the correct phrase: 'To call it a day' means ______.",
            "options": ["To start a work", "To stop working on something", "To name a day", "To have a holiday"],
            "correct_option": "To stop working on something",
            "difficulty_level": "Hard",
            "solution_steps": "The idiom 'call it a day' means to stop what you are doing for the day.",
            "explanation_description": "Idioms."
        },
        {
            "question_text": "Choose the correct option: If Rohit is 'fast', and Sumit is 'faster', then Amit, who won the race, is the ______.",
            "options": ["fastest", "most fast", "more fast", "fasted"],
            "correct_option": "fastest",
            "difficulty_level": "Medium",
            "solution_steps": "For comparing three or more entities, the superlative degree 'fastest' is used.",
            "explanation_description": "Degrees of comparison."
        },
        {
            "question_text": "What is the synonym of 'courage'?",
            "options": ["Fear", "Cowardice", "Bravery", "Weakness"],
            "correct_option": "Bravery",
            "difficulty_level": "Medium",
            "solution_steps": "Courage is synonymous with bravery.",
            "explanation_description": "Synonyms."
        },
        {
            "question_text": "What is the plural of 'sheep'?",
            "options": ["Sheeps", "Sheep", "Sheepes", "Ship"],
            "correct_option": "Sheep",
            "difficulty_level": "Medium",
            "solution_steps": "The noun 'sheep' remains the same in both singular and plural forms.",
            "explanation_description": "Irregular plurals."
        },
        {
            "question_text": "Fill in the blank with the correct preposition: We should be kind ______ animals.",
            "options": ["to", "with", "at", "for"],
            "correct_option": "to",
            "difficulty_level": "Medium",
            "solution_steps": "The standard preposition collocation is 'kind to' someone or something.",
            "explanation_description": "Preposition collocations."
        },
        {
            "question_text": "Which word is a homophone of 'write'?",
            "options": ["Right", "Rode", "Rate", "Rote"],
            "correct_option": "Right",
            "difficulty_level": "Easy",
            "solution_steps": "Right and write are pronounced exactly the same but spelled differently.",
            "explanation_description": "Homophones."
        },
        {
            "question_text": "Choose the correct word: 'A group of ships is called a ______.'",
            "options": ["fleet", "pack", "herd", "bunch"],
            "correct_option": "fleet",
            "difficulty_level": "Medium",
            "solution_steps": "The collective noun for ships is 'fleet'.",
            "explanation_description": "Collective nouns."
        },
        {
            "question_text": "Choose the correct spelling:",
            "options": ["Beautiful", "Beatiful", "Beautifull", "Butiful"],
            "correct_option": "Beautiful",
            "difficulty_level": "Easy",
            "solution_steps": "The correct spelling is B-E-A-U-T-I-F-U-L.",
            "explanation_description": "Spellings."
        },
        {
            "question_text": "Choose the correct pronoun: 'Who is that girl? Do you know ______?'",
            "options": ["her", "she", "hers", "him"],
            "correct_option": "her",
            "difficulty_level": "Easy",
            "solution_steps": "The object pronoun for a female singular subject is 'her'.",
            "explanation_description": "Object pronouns."
        },
        {
            "question_text": "Identify the adverb in: 'The children played happily in the garden.'",
            "options": ["children", "played", "happily", "garden"],
            "correct_option": "happily",
            "difficulty_level": "Easy",
            "solution_steps": "'happily' modifies the verb 'played', describing how they played.",
            "explanation_description": "Adverbs."
        },
        {
            "question_text": "Choose the correct spelling for the day of the week that comes after Tuesday.",
            "options": ["Wensday", "Wednesday", "Wedensday", "Wednesdey"],
            "correct_option": "Wednesday",
            "difficulty_level": "Easy",
            "solution_steps": "The correct spelling is W-E-D-N-E-S-D-A-Y.",
            "explanation_description": "Spellings."
        },
        {
            "question_text": "Choose the correct word: A person who writes books is an ______.",
            "options": ["artist", "author", "actor", "agent"],
            "correct_option": "author",
            "difficulty_level": "Easy",
            "solution_steps": "An author writes literature/books.",
            "explanation_description": "Vocabulary."
        }
    ]

def populate_ieo_quizzes_direct():
    print("Starting direct IEO Grade 3 quiz population...")
    
    sections = [
        {"name": "Word and Structure Knowledge", "data": get_word_structure_knowledge()},
        {"name": "Reading", "data": get_reading()},
        {"name": "Spoken and Written Expression", "data": get_spoken_written_expression()},
        {"name": "Achievers Section", "data": get_achievers_section()}
    ]
    
    quiz_table = "olympiad_quizzes"
    question_table = "olympiad_questions"
    fk_field = "olympiad_quiz_id"
    
    for sec in sections:
        section_name = sec["name"]
        questions = sec["data"]
        print(f"\nProcessing section: {section_name}")
        
        # Check if quiz already exists
        existing_meta = supabase_db.table(quiz_table).select("id").eq("board", "CBSE").eq("grade", "Grade 3").eq("subject", "IEO Test").eq("chapter_or_topic", section_name).execute()
        if existing_meta.data:
            existing_id = existing_meta.data[0]["id"]
            print(f"Existing quiz found (ID: {existing_id}). Deleting old questions and quiz...")
            supabase_db.table(question_table).delete().eq(fk_field, existing_id).execute()
            supabase_db.table(quiz_table).delete().eq("id", existing_id).execute()
            
        # Create new quiz row
        quiz_metadata = {
            "board": "CBSE",
            "grade": "Grade 3",
            "subject": "IEO Test",
            "chapter_or_topic": section_name
        }
        quiz_res = supabase_db.table(quiz_table).insert(quiz_metadata).execute()
        if not quiz_res.data:
            print(f"Failed to create quiz for {section_name}")
            continue
            
        new_quiz_id = quiz_res.data[0]["id"]
        print(f"Created new quiz in DB with ID: {new_quiz_id}")
        
        questions_payload = []
        for q in questions:
            questions_payload.append({
                fk_field: new_quiz_id,
                "question_text": q["question_text"],
                "question_type": "MCQ",
                "difficulty_level": q["difficulty_level"],
                "options": q["options"],
                "correct_option": q["correct_option"],
                "solution_steps": q["solution_steps"],
                "explanation_description": q["explanation_description"]
            })
            
        res_insert = supabase_db.table(question_table).insert(questions_payload).execute()
        if res_insert.data:
            print(f"Successfully saved {len(res_insert.data)} questions for {section_name}")
        else:
            print(f"Failed to save questions for {section_name}")

if __name__ == "__main__":
    populate_ieo_quizzes_direct()
