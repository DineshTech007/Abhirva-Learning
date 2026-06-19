import os
import sys

# Ensure the backend directory is in the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.supabase_client import supabase_db

def get_logical_reasoning():
    return [
        {
            "question_text": "Which of the following numbers will replace the question mark (?) in the pattern: 3, 6, 12, 24, ?, 96?",
            "options": ["36", "48", "60", "72"],
            "correct_option": "48",
            "difficulty_level": "Easy",
            "solution_steps": "Each term is multiplied by 2: 3*2=6, 6*2=12, 12*2=24, 24*2=48, 48*2=96. So the missing number is 48.",
            "explanation_description": "Geometric progression pattern."
        },
        {
            "question_text": "If 'APPLE' is coded as 'BQQMF' in a code language, how will 'GRAPE' be coded?",
            "options": ["HSBQF", "HQAPF", "HSAQF", "HRBPF"],
            "correct_option": "HSBQF",
            "difficulty_level": "Easy",
            "solution_steps": "Each letter in APPLE is shifted +1 to get BQQMF. Similarly, for GRAPE: G->H, R->S, A->B, P->Q, E->F. The code is HSBQF.",
            "explanation_description": "Letter shift coding."
        },
        {
            "question_text": "Ravi is standing in a queue. He is 7th from the front and 9th from the back. How many people are in the queue?",
            "options": ["16", "15", "17", "14"],
            "correct_option": "15",
            "difficulty_level": "Medium",
            "solution_steps": "Total people = position from front + position from back - 1 = 7 + 9 - 1 = 15.",
            "explanation_description": "Queue ordering calculation."
        },
        {
            "question_text": "Find the odd one out among the given options:",
            "options": ["Square", "Rectangle", "Circle", "Triangle"],
            "correct_option": "Circle",
            "difficulty_level": "Easy",
            "solution_steps": "Square, Rectangle, and Triangle are formed of straight line segments, whereas a Circle is a closed curved shape.",
            "explanation_description": "Shape classification."
        },
        {
            "question_text": "Identify the mirror image of the letter 'F' when mirror is placed to its right.",
            "options": ["F", "flipped F (facing left)", "E", "inverted F (upside down)"],
            "correct_option": "flipped F (facing left)",
            "difficulty_level": "Easy",
            "solution_steps": "The vertical bar remains on the left, and the horizontal bars face the mirror (leftwards). So it is flipped horizontally.",
            "explanation_description": "Mirror reflection."
        },
        {
            "question_text": "Which shape replaces the question mark (?) in: Circle:1 :: Triangle:3 :: Square:?",
            "options": ["2", "4", "5", "6"],
            "correct_option": "4",
            "difficulty_level": "Easy",
            "solution_steps": "Circle has 1 curved face/boundary, Triangle has 3 sides, Square has 4 sides. The correct count is 4.",
            "explanation_description": "Shape attribute analogy."
        },
        {
            "question_text": "If today is Saturday, what day was it 4 days before yesterday?",
            "options": ["Tuesday", "Monday", "Wednesday", "Sunday"],
            "correct_option": "Monday",
            "difficulty_level": "Medium",
            "solution_steps": "Today is Saturday. Yesterday was Friday. 4 days before Friday was: Thursday (1), Wednesday (2), Tuesday (3), Monday (4).",
            "explanation_description": "Day offset reasoning."
        },
        {
            "question_text": "How many squares are there in a grid of size 3x1?",
            "options": ["3", "4", "2", "5"],
            "correct_option": "3",
            "difficulty_level": "Easy",
            "solution_steps": "A 3x1 grid contains exactly 3 individual 1x1 squares.",
            "explanation_description": "Square counting."
        },
        {
            "question_text": "Choose the next letter in the series: A, C, E, G, ?",
            "options": ["H", "I", "J", "K"],
            "correct_option": "I",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern skips one letter each time: A (+2)-> C (+2)-> E (+2)-> G (+2)-> I.",
            "explanation_description": "Alphabet progression."
        },
        {
            "question_text": "A bird starts flying North. It turns right, then turns right again. Which direction is the bird facing now?",
            "options": ["East", "West", "South", "North"],
            "correct_option": "South",
            "difficulty_level": "Medium",
            "solution_steps": "Starts North. Turns right -> facing East. Turns right again -> facing South.",
            "explanation_description": "Direction mapping."
        },
        {
            "question_text": "How many groups of 3 stars each can be formed from 15 stars?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "5",
            "difficulty_level": "Easy",
            "solution_steps": "Number of groups = Total stars / Stars per group = 15 / 3 = 5.",
            "explanation_description": "Grouping and division."
        },
        {
            "question_text": "In a certain code, 'FISH' is written as 'EHRG'. How is 'JUNGLE' written in that code?",
            "options": ["ITMDKD", "ITMFKD", "ITMELD", "IUMFKD"],
            "correct_option": "ITMFKD",
            "difficulty_level": "Hard",
            "solution_steps": "Each letter is shifted -1: F->E, I->H, S->R, H->G. For JUNGLE: J->I, U->T, N->M, G->F, L->K, E->D. The code is ITMFKD.",
            "explanation_description": "Letter shift cipher (-1)."
        },
        {
            "question_text": "Find the missing number in the grid:\n[ 3 ] [ 6 ] [ 9 ]\n[ 5 ] [ 10 ] [ ? ]",
            "options": ["12", "15", "18", "20"],
            "correct_option": "15",
            "difficulty_level": "Medium",
            "solution_steps": "Row 1: 3, 6, 9 (multiples of 3). Row 2: 5, 10, 15 (multiples of 5). The missing number is 15.",
            "explanation_description": "Grid number patterns."
        },
        {
            "question_text": "A clock shows 6:00. The hour hand points South. In which direction does the minute hand point?",
            "options": ["North", "South", "East", "West"],
            "correct_option": "North",
            "difficulty_level": "Easy",
            "solution_steps": "At 6:00, the hour hand points down at 6 (South), and the minute hand points up at 12 (North).",
            "explanation_description": "Clock hands direction."
        },
        {
            "question_text": "Identify the odd letter-group out of the following:",
            "options": ["ABC", "XYZ", "PQR", "KMN"],
            "correct_option": "KMN",
            "difficulty_level": "Medium",
            "solution_steps": "ABC, XYZ, and PQR consist of consecutive alphabets. KMN has a skip of L (K->L->M->N).",
            "explanation_description": "Alphabet group criteria."
        },
        {
            "question_text": "If a circle represents 5, a square represents 10, and a triangle represents 15, what is the value of: Triangle - Circle + Square?",
            "options": ["20", "15", "30", "25"],
            "correct_option": "20",
            "difficulty_level": "Easy",
            "solution_steps": "Value = 15 - 5 + 10 = 10 + 10 = 20.",
            "explanation_description": "Symbol arithmetic substitution."
        },
        {
            "question_text": "How many vertices does a standard triangular pyramid (tetrahedron) have?",
            "options": ["4", "5", "6", "3"],
            "correct_option": "4",
            "difficulty_level": "Medium",
            "solution_steps": "A triangular pyramid has a triangular base (3 vertices) and 1 top vertex. Total = 4 vertices.",
            "explanation_description": "3D shape properties."
        },
        {
            "question_text": "If pencil is called eraser, eraser is called sharpener, and sharpener is called bag, what do we use to correct our mistakes on paper?",
            "options": ["pencil", "eraser", "sharpener", "bag"],
            "correct_option": "sharpener",
            "difficulty_level": "Medium",
            "solution_steps": "We use an eraser to correct mistakes. In this code, eraser is called sharpener. So the correct option is sharpener.",
            "explanation_description": "Word substitution logic."
        },
        {
            "question_text": "Which of these figures can be fully embedded inside a larger circle?",
            "options": ["Square", "Line longer than diameter", "Large pentagon", "Rectangle wider than diameter"],
            "correct_option": "Square",
            "difficulty_level": "Easy",
            "solution_steps": "A square can be drawn inside a circle if its diagonal is less than the diameter. Other options are larger than the circle.",
            "explanation_description": "Embedded spatial shapes."
        },
        {
            "question_text": "Four children (A, B, C, D) participated in a race. A finished before B. C finished after B. D finished before A. Who won the race?",
            "options": ["A", "B", "C", "D"],
            "correct_option": "D",
            "difficulty_level": "Medium",
            "solution_steps": "D finished before A, A finished before B, B finished before C. The order is D -> A -> B -> C. D finished first.",
            "explanation_description": "Comparative logic ranking."
        },
        {
            "question_text": "What is the missing shape in the pattern: ◯, ▢, ◯, ▢, ?, ▢?",
            "options": ["◯", "▢", "▵", "◇"],
            "correct_option": "◯",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern alternates between circle (◯) and square (▢). The missing term must be a circle (◯).",
            "explanation_description": "Alternate repeating shapes."
        },
        {
            "question_text": "A cube has how many edges?",
            "options": ["6", "8", "12", "10"],
            "correct_option": "12",
            "difficulty_level": "Easy",
            "solution_steps": "A cube consists of 6 faces, 8 vertices, and 12 straight edges.",
            "explanation_description": "Cube properties."
        },
        {
            "question_text": "Complete the analogy: Feather:Light :: Stone:_________",
            "options": ["Soft", "Heavy", "Floating", "Cold"],
            "correct_option": "Heavy",
            "difficulty_level": "Easy",
            "solution_steps": "A feather is characterized as being light in weight, while a stone is heavy.",
            "explanation_description": "Object-property analogy."
        },
        {
            "question_text": "How many days are there in 5 weeks?",
            "options": ["30 days", "35 days", "40 days", "28 days"],
            "correct_option": "35 days",
            "difficulty_level": "Easy",
            "solution_steps": "1 week = 7 days. 5 weeks = 5 * 7 = 35 days.",
            "explanation_description": "Calendar math."
        },
        {
            "question_text": "If 'RED' is coded as '27', how is 'BLUE' coded if letters represent their position values added together (A=1, B=2, C=3, etc.)?",
            "options": ["40", "36", "38", "42"],
            "correct_option": "40",
            "difficulty_level": "Hard",
            "solution_steps": "B=2, L=12, U=21, E=5. Sum = 2 + 12 + 21 + 5 = 40.",
            "explanation_description": "Alphabet position summing."
        },
        {
            "question_text": "A sheet of paper has 4 corners. If you cut off one corner with a straight cut, how many corners does the paper have now?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "5",
            "difficulty_level": "Hard",
            "solution_steps": "Cutting off one corner replaces the 1 corner with 2 new corners. Total corners = 4 - 1 + 2 = 5 corners.",
            "explanation_description": "Spatial cutting puzzle."
        },
        {
            "question_text": "Identify the letter that occupies the middle position when the word 'OLYMPIAD' is arranged in alphabetical order.",
            "options": ["M", "I", "L", "D"],
            "correct_option": "L",
            "difficulty_level": "Hard",
            "solution_steps": "Word: OLYMPIAD. Letters: A, D, I, L, M, O, P, Y (8 letters). The middle positions are L and M. Out of options, L is correct.",
            "explanation_description": "Alphabetical sorting logic."
        },
        {
            "question_text": "If you are facing North and you turn 180 degrees, which direction are you facing?",
            "options": ["East", "West", "South", "North"],
            "correct_option": "South",
            "difficulty_level": "Easy",
            "solution_steps": "A turn of 180 degrees points you in the exact opposite direction. Opposite of North is South.",
            "explanation_description": "Direction rotation."
        },
        {
            "question_text": "How many triangles can you find in a standard 5-pointed star?",
            "options": ["5", "10", "8", "6"],
            "correct_option": "10",
            "difficulty_level": "Hard",
            "solution_steps": "A 5-pointed star contains 5 small triangles (points) and 5 large triangles (overlapping inside). Total is 10 triangles.",
            "explanation_description": "Complex geometry counting."
        },
        {
            "question_text": "If ⏶ represents 5 units and ◯ represents 10 units, what represents 25 units?",
            "options": ["⏶ + ◯", "⏶ + ⏶ + ◯", "◯ + ◯", "⏶ + ⏶ + ⏶ + ◯"],
            "correct_option": "⏶ + ⏶ + ◯",
            "difficulty_level": "Medium",
            "solution_steps": "5 + 5 + 10 = 20... wait, ⏶ + ⏶ + ◯ is 5 + 5 + 10 = 20. ⏶ + ⏶ + ⏶ + ◯ is 5 + 5 + 5 + 10 = 25. The correct option is ⏶ + ⏶ + ⏶ + ◯.",
            "options": ["⏶ + ◯", "◯ + ◯", "⏶ + ⏶ + ⏶ + ◯", "⏶ + ◯ + ◯"],
            "correct_option": "⏶ + ◯ + ◯",
            "difficulty_level": "Medium",
            "solution_steps": "5 + 10 + 10 = 25. Thus, ⏶ + ◯ + ◯ is the correct representation.",
            "explanation_description": "Symbolic representation representation."
        }
    ]

def get_science():
    return [
        {
            "question_text": "Which part of the plant holds the plant firmly in the soil and absorbs water and minerals?",
            "options": ["Stem", "Root", "Leaf", "Flower"],
            "correct_option": "Root",
            "difficulty_level": "Easy",
            "solution_steps": "Roots grow underground. They hold the plant in the soil and absorb water and nutrients.",
            "explanation_description": "Plant parts and functions."
        },
        {
            "question_text": "Plants make their own food in their leaves. What is this process called?",
            "options": ["Respiration", "Photosynthesis", "Transpiration", "Germination"],
            "correct_option": "Photosynthesis",
            "difficulty_level": "Medium",
            "solution_steps": "Photosynthesis is the process by which green plants make food using sunlight, carbon dioxide, and water.",
            "explanation_description": "Plant physiology."
        },
        {
            "question_text": "Which of the following birds has a strong, chisel-shaped beak to drill holes in tree trunks to find insects?",
            "options": ["Hummingbird", "Woodpecker", "Sparrow", "Duck"],
            "correct_option": "Woodpecker",
            "difficulty_level": "Medium",
            "solution_steps": "A woodpecker has a strong, sharp, chisel-shaped beak to peck at tree bark and drill holes for food.",
            "explanation_description": "Bird adaptions - beaks."
        },
        {
            "question_text": "Which food group is rich in proteins and helps our body grow and repair damaged parts?",
            "options": ["Energy-giving food", "Body-building food", "Protective food", "Junk food"],
            "correct_option": "Body-building food",
            "difficulty_level": "Easy",
            "solution_steps": "Proteins are body-building nutrients that help in growth and tissue repair.",
            "explanation_description": "Food and nutrition."
        },
        {
            "question_text": "Which of the following materials is transparent, allowing light to pass through it fully?",
            "options": ["Wood", "Clear Glass", "Cardboard", "Iron Sheet"],
            "correct_option": "Clear Glass",
            "difficulty_level": "Easy",
            "solution_steps": "Transparent materials like clear glass allow light to pass through them, so objects behind them are visible.",
            "explanation_description": "Matter and material properties."
        },
        {
            "question_text": "Which gas do human beings breathe in during respiration?",
            "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"],
            "correct_option": "Oxygen",
            "difficulty_level": "Easy",
            "solution_steps": "Humans inhale oxygen and exhale carbon dioxide.",
            "explanation_description": "Human body systems."
        },
        {
            "question_text": "Which planet is known as the 'Blue Planet' because of the presence of water on its surface?",
            "options": ["Mars", "Venus", "Earth", "Jupiter"],
            "correct_option": "Earth",
            "difficulty_level": "Easy",
            "solution_steps": "Earth appears blue from space because water covers about 71% of its surface.",
            "explanation_description": "Earth and space science."
        },
        {
            "question_text": "Water exists in three states: solid, liquid, and gas. What is the gaseous state of water called?",
            "options": ["Ice", "Water vapor", "Dew", "Snow"],
            "correct_option": "Water vapor",
            "difficulty_level": "Easy",
            "solution_steps": "The gaseous state of water is water vapor or steam.",
            "explanation_description": "States of matter."
        },
        {
            "question_text": "What is the primary source of light and heat on Earth?",
            "options": ["Moon", "Sun", "Stars", "Electricity"],
            "correct_option": "Sun",
            "difficulty_level": "Easy",
            "solution_steps": "The Sun is the ultimate natural source of light and energy for the Earth.",
            "explanation_description": "Light and heat sources."
        },
        {
            "question_text": "Which of the following forces opposes motion when two surfaces touch each other?",
            "options": ["Magnetic force", "Gravitational force", "Frictional force", "Electrostatic force"],
            "correct_option": "Frictional force",
            "difficulty_level": "Medium",
            "solution_steps": "Friction is the force that opposes the relative motion of two surfaces in contact.",
            "explanation_description": "Force and motion."
        },
        {
            "question_text": "Which type of pollution is caused by excessive smoke from cars and factories?",
            "options": ["Water pollution", "Air pollution", "Soil pollution", "Noise pollution"],
            "correct_option": "Air pollution",
            "difficulty_level": "Easy",
            "solution_steps": "Smoke contains harmful gases and particles that contaminate the air, causing air pollution.",
            "explanation_description": "Environmental science."
        },
        {
            "question_text": "Which of the following animals undergoes metamorphosis during its life cycle?",
            "options": ["Dog", "Cat", "Butterfly", "Cow"],
            "correct_option": "Butterfly",
            "difficulty_level": "Medium",
            "solution_steps": "A butterfly goes through egg, larva (caterpillar), pupa (chrysalis), and adult stages, which is called metamorphosis.",
            "explanation_description": "Animal life cycles."
        },
        {
            "question_text": "Which organ system helps in breaking down food into simple substances that our body can use?",
            "options": ["Respiratory system", "Circulatory system", "Digestive system", "Nervous system"],
            "correct_option": "Digestive system",
            "difficulty_level": "Easy",
            "solution_steps": "The digestive system processes food so nutrients can be absorbed by the body.",
            "explanation_description": "Human organ systems."
        },
        {
            "question_text": "What is the circular movement of water from Earth's surface to the sky and back called?",
            "options": ["Rock cycle", "Water cycle", "Carbon cycle", "Life cycle"],
            "correct_option": "Water cycle",
            "difficulty_level": "Easy",
            "solution_steps": "The water cycle involves evaporation, condensation, precipitation, and collection.",
            "explanation_description": "Water cycle phenomena."
        },
        {
            "question_text": "Which of these birds cannot fly but can run very fast?",
            "options": ["Eagle", "Pigeon", "Ostrich", "Crow"],
            "correct_option": "Ostrich",
            "difficulty_level": "Easy",
            "solution_steps": "The ostrich is a flightless bird with strong legs adapted for fast running.",
            "explanation_description": "Bird adaptations."
        },
        {
            "question_text": "Which of the following is a non-living thing that was once part of a living thing?",
            "options": ["Plastic bottle", "Wooden table", "Glass tumbler", "Steel spoon"],
            "correct_option": "Wooden table",
            "difficulty_level": "Medium",
            "solution_steps": "Wood comes from trees, which are living things. So a wooden table was once part of a living thing.",
            "explanation_description": "Living and non-living characteristics."
        },
        {
            "question_text": "Which safety rule should you follow while walking on the road?",
            "options": ["Walk in the middle of the road", "Walk on the footpath", "Run across when vehicles are moving", "Play games on the road"],
            "correct_option": "Walk on the footpath",
            "difficulty_level": "Easy",
            "solution_steps": "Walking on the footpath ensures safety from vehicles on the road.",
            "explanation_description": "Safety rules."
        },
        {
            "question_text": "Which component of soil is formed from decayed plants and animals, making it fertile?",
            "options": ["Sand", "Clay", "Humus", "Gravel"],
            "correct_option": "Humus",
            "difficulty_level": "Medium",
            "solution_steps": "Humus is the dark, organic material in soil created by decaying organic matter, providing essential nutrients.",
            "explanation_description": "Soil science."
        },
        {
            "question_text": "When an object blocks the path of light, what is formed on the opposite side?",
            "options": ["Reflection", "Rainbow", "Shadow", "Beam"],
            "correct_option": "Shadow",
            "difficulty_level": "Easy",
            "solution_steps": "Light travels in straight lines. If an opaque object blocks it, a dark space called a shadow is formed.",
            "explanation_description": "Light and shadow properties."
        },
        {
            "question_text": "What type of clothes keep us warm and protect us during cold winters?",
            "options": ["Cotton clothes", "Woolen clothes", "Silk clothes", "Nylon clothes"],
            "correct_option": "Woolen clothes",
            "difficulty_level": "Easy",
            "solution_steps": "Woolen clothes trap air, which is a poor conductor of heat, keeping our body warm in winter.",
            "explanation_description": "Housing and clothing."
        },
        {
            "question_text": "Which organ in our body pumps blood to all other parts?",
            "options": ["Brain", "Lungs", "Heart", "Stomach"],
            "correct_option": "Heart",
            "difficulty_level": "Easy",
            "solution_steps": "The heart is a muscular organ that pumps oxygenated and nutrient-rich blood throughout the body.",
            "explanation_description": "Human anatomy - circulatory."
        },
        {
            "question_text": "Which of these is a natural fiber obtained from a plant source?",
            "options": ["Nylon", "Cotton", "Wool", "Polyester"],
            "correct_option": "Cotton",
            "difficulty_level": "Easy",
            "solution_steps": "Cotton comes from cotton plants. Nylon and polyester are synthetic, and wool comes from animals.",
            "explanation_description": "Materials and fibers."
        },
        {
            "question_text": "Which celestial body does not have its own light but reflects sunlight?",
            "options": ["Sun", "Moon", "Star", "Sirius"],
            "correct_option": "Moon",
            "difficulty_level": "Easy",
            "solution_steps": "The Moon does not emit light. It shines because it reflects light from the Sun.",
            "explanation_description": "Astronomy basics."
        },
        {
            "question_text": "Which of the following animals has webbed feet to swim in water?",
            "options": ["Sparrow", "Eagle", "Duck", "Parrot"],
            "correct_option": "Duck",
            "difficulty_level": "Easy",
            "solution_steps": "Ducks have webbed feet that act like paddles to help them swim.",
            "explanation_description": "Animal adaptation - locomotion."
        },
        {
            "question_text": "Which of the following is a healthy eating habit?",
            "options": ["Eating uncovered food", "Chewing food properly", "Eating lots of junk food", "Skipping meals daily"],
            "correct_option": "Chewing food properly",
            "difficulty_level": "Easy",
            "solution_steps": "Chewing food thoroughly helps in saliva mixing and smooth digestion.",
            "explanation_description": "Health and hygiene."
        },
        {
            "question_text": "What is the layer of gases surrounding the Earth called?",
            "options": ["Hydrosphere", "Lithosphere", "Atmosphere", "Biosphere"],
            "correct_option": "Atmosphere",
            "difficulty_level": "Medium",
            "solution_steps": "The atmosphere is the blanket of air held around the Earth by gravity.",
            "explanation_description": "Earth system layers."
        },
        {
            "question_text": "Which of these animals live in water and breathe through gills?",
            "options": ["Whale", "Fish", "Dolphin", "Frog"],
            "correct_option": "Fish",
            "difficulty_level": "Medium",
            "solution_steps": "Fish absorb dissolved oxygen from water through their gills. Whales and dolphins breathe through lungs and blowholes.",
            "explanation_description": "Animal breathing organs."
        },
        {
            "question_text": "What type of force are you using when you pull open a drawer?",
            "options": ["Pushing force", "Pulling force", "Frictional force", "Gravitational force"],
            "correct_option": "Pulling force",
            "difficulty_level": "Easy",
            "solution_steps": "Drawing something towards yourself is a pull.",
            "explanation_description": "Force concepts."
        },
        {
            "question_text": "Which of the following leaves has a medicinal value and is commonly used to treat cough and cold?",
            "options": ["Lotus leaf", "Tulsi leaf", "Rose leaf", "Banana leaf"],
            "correct_option": "Tulsi leaf",
            "difficulty_level": "Easy",
            "solution_steps": "Tulsi (basil) leaves have strong antiseptic and medicinal properties used in traditional medicine for colds.",
            "explanation_description": "Plants usage."
        },
        {
            "question_text": "Which bird builds its nest by stitching leaves together using spider webs or threads?",
            "options": ["Weaver bird", "Tailor bird", "Woodpecker", "Penguin"],
            "correct_option": "Tailor bird",
            "difficulty_level": "Medium",
            "solution_steps": "A tailor bird stitches leaves together with its beak using plant fibers or silk threads, hence the name.",
            "explanation_description": "Nesting behavior."
        },
        {
            "question_text": "Which state of matter has a fixed volume but no fixed shape, taking the shape of its container?",
            "options": ["Solid", "Liquid", "Gas", "All of these"],
            "correct_option": "Liquid",
            "difficulty_level": "Medium",
            "solution_steps": "Liquids flow to fit their container's shape, but their total volume remains constant.",
            "explanation_description": "States of matter properties."
        },
        {
            "question_text": "Which of the following is a means of mass communication, sending information to many people at once?",
            "options": ["Telephone", "Letter", "Newspaper", "Postcard"],
            "correct_option": "Newspaper",
            "difficulty_level": "Medium",
            "solution_steps": "Newspapers, TV, and Radio reach a large audience simultaneously (mass communication).",
            "explanation_description": "Communication systems."
        },
        {
            "question_text": "Which organ in our body is responsible for thinking, memory, and control?",
            "options": ["Heart", "Lungs", "Brain", "Kidneys"],
            "correct_option": "Brain",
            "difficulty_level": "Easy",
            "solution_steps": "The brain coordinates bodily actions, processes thoughts, and stores memories.",
            "explanation_description": "Human nervous system."
        },
        {
            "question_text": "What happens to ice when it is heated?",
            "options": ["It freezes", "It melts into water", "It turns to steam directly", "It does not change"],
            "correct_option": "It melts into water",
            "difficulty_level": "Easy",
            "solution_steps": "Heating ice raises its temperature above freezing, causing it to change from solid to liquid water (melting).",
            "explanation_description": "Thermal change of state."
        },
        {
            "question_text": "Which gas is released by plants during photosynthesis, which is essential for animals to survive?",
            "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Argon"],
            "correct_option": "Oxygen",
            "difficulty_level": "Easy",
            "solution_steps": "Plants release oxygen as a byproduct of food making, which animals inhale.",
            "explanation_description": "Photosynthesis output."
        },
        {
            "question_text": "Which of these birds uses its beak to catch fish from the water and has a pouch under its bill?",
            "options": ["Parrot", "Pelican", "Eagle", "Hummingbird"],
            "correct_option": "Pelican",
            "difficulty_level": "Hard",
            "solution_steps": "Pelicans have large throat pouches to scoop up water and trap fish.",
            "explanation_description": "Bird adaptations."
        },
        {
            "question_text": "Which component of air is present in the largest quantity?",
            "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Water vapor"],
            "correct_option": "Nitrogen",
            "difficulty_level": "Medium",
            "solution_steps": "Nitrogen makes up about 78% of the Earth's atmosphere.",
            "explanation_description": "Air composition."
        },
        {
            "question_text": "Which type of house is made of snow blocks and is found in extremely cold regions?",
            "options": ["Igloo", "Caravan", "Houseboat", "Tent"],
            "correct_option": "Igloo",
            "difficulty_level": "Easy",
            "solution_steps": "Igloos are dome-shaped shelters constructed from blocks of compacted snow.",
            "explanation_description": "Housing types."
        },
        {
            "question_text": "Which nutrient provides instant energy to our body?",
            "options": ["Proteins", "Vitamins", "Carbohydrates", "Minerals"],
            "correct_option": "Carbohydrates",
            "difficulty_level": "Medium",
            "solution_steps": "Carbohydrates are the body's primary and quickest fuel source.",
            "explanation_description": "Nutrients classification."
        },
        {
            "question_text": "Which of the following activities helps in reducing environmental pollution?",
            "options": ["Cutting down trees", "Burning plastic wastes", "Planting more trees", "Wasting water"],
            "correct_option": "Planting more trees",
            "difficulty_level": "Easy",
            "solution_steps": "Afforestation (planting trees) absorbs carbon dioxide and purifies the air.",
            "explanation_description": "Environmental conservation."
        },
        {
            "question_text": "What type of sound is generally pleasant to our ears?",
            "options": ["Car honking", "Loud music", "Chirping of birds", "Drilling machine"],
            "correct_option": "Chirping of birds",
            "difficulty_level": "Easy",
            "solution_steps": "Bird chirping is soft and pleasant. Car horns and drills are loud noise pollution.",
            "explanation_description": "Light, sound and force."
        },
        {
            "question_text": "Which system of our body is made up of bones and gives shape and support to the body?",
            "options": ["Muscular system", "Skeletal system", "Nervous system", "Digestive system"],
            "correct_option": "Skeletal system",
            "difficulty_level": "Easy",
            "solution_steps": "The skeleton is the framework of bones that provides structural support and protects organs.",
            "explanation_description": "Human skeletal system."
        },
        {
            "question_text": "Which of the following is a herbivorous animal, eating only plants?",
            "options": ["Lion", "Tiger", "Rabbit", "Vulture"],
            "correct_option": "Rabbit",
            "difficulty_level": "Easy",
            "solution_steps": "Rabbits consume grasses and leafy green plants, classifying them as herbivores.",
            "explanation_description": "Animal diets."
        },
        {
            "question_text": "How many sensory organs do humans have?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "5",
            "difficulty_level": "Easy",
            "solution_steps": "Humans have 5 sense organs: eyes, ears, nose, tongue, and skin.",
            "explanation_description": "Human senses."
        },
        {
            "question_text": "Which of the following is a man-made material?",
            "options": ["Wood", "Plastic", "Cotton", "Coal"],
            "correct_option": "Plastic",
            "difficulty_level": "Easy",
            "solution_steps": "Plastic is synthesized in factories from petrochemical chemicals.",
            "explanation_description": "Natural vs synthetic materials."
        },
        {
            "question_text": "Which safety device is worn in a car to prevent injury during sudden breaks?",
            "options": ["Helmet", "Seatbelt", "Goggles", "Life jacket"],
            "correct_option": "Seatbelt",
            "difficulty_level": "Easy",
            "solution_steps": "Seatbelts hold passengers securely in place, minimizing forward movement during deceleration.",
            "explanation_description": "Safety rules."
        },
        {
            "question_text": "What type of weather is associated with dark clouds, thunder, and heavy rainfall?",
            "options": ["Sunny day", "Stormy day", "Windy day", "Foggy day"],
            "correct_option": "Stormy day",
            "difficulty_level": "Easy",
            "solution_steps": "Storms bring strong winds, thunder, lightning, and downpours.",
            "explanation_description": "Weather conditions."
        },
        {
            "question_text": "Which of the following animals changes its skin color to match its surroundings for protection?",
            "options": ["Zebra", "Chameleon", "Giraffe", "Elephant"],
            "correct_option": "Chameleon",
            "difficulty_level": "Easy",
            "solution_steps": "Chameleons camouflage by shifting skin pigments to blend with foliage or branches.",
            "explanation_description": "Animal camouflage."
        },
        {
            "question_text": "What is the process called where waste materials are converted into useful new items?",
            "options": ["Reducing", "Reusing", "Recycling", "Refusing"],
            "correct_option": "Recycling",
            "difficulty_level": "Medium",
            "solution_steps": "Recycling turns old materials (like glass, paper, cans) into raw materials for new products.",
            "explanation_description": "Waste management."
        },
        {
            "question_text": "Which force pulls everything down towards the center of the Earth?",
            "options": ["Magnetic force", "Frictional force", "Gravitational force", "Muscle force"],
            "correct_option": "Gravitational force",
            "difficulty_level": "Easy",
            "solution_steps": "Gravity is the attractive force that acts between all objects with mass, pulling them downward.",
            "explanation_description": "Gravitational force."
        }
    ]

def get_achievers_section():
    return [
        {
            "question_text": "Refer to the table about material properties and select the correct statement:\nMaterial P: Flexible=No, Waterproof=Yes, Floats=No\nMaterial Q: Flexible=Yes, Waterproof=Yes, Floats=Yes\nMaterial R: Flexible=Yes, Waterproof=No, Floats=Yes",
            "options": ["P can be a steel spoon and Q can be a rubber band", "Q can be a wooden block and R can be a paper sheet", "P can be a clay brick and Q can be a plastic toy boat", "R can be a glass bottle and P can be a sponge"],
            "correct_option": "P can be a clay brick and Q can be a plastic toy boat",
            "difficulty_level": "Hard",
            "solution_steps": "P is rigid (Flexible=No), waterproof, sinks (Floats=No) -> matching clay brick. Q is flexible, waterproof, floats -> plastic toy boat.",
            "explanation_description": "Material properties matrix."
        },
        {
            "question_text": "Read the following statements and choose the correct option:\nStatement 1: Plants clean the air by consuming oxygen during the day.\nStatement 2: Stomata are tiny pores on leaves that help in gas exchange.",
            "options": ["Both statements are correct", "Both statements are incorrect", "Statement 1 is correct, Statement 2 is incorrect", "Statement 1 is incorrect, Statement 2 is correct"],
            "correct_option": "Statement 1 is incorrect, Statement 2 is correct",
            "difficulty_level": "Hard",
            "solution_steps": "Plants clean the air by absorbing carbon dioxide and releasing oxygen during photosynthesis. Stomata are indeed pores for transpiration and respiration.",
            "explanation_description": "Dual statement validation."
        },
        {
            "question_text": "Match the following occupations with the tools they use:\na. Electrician  - 1. Stethoscope\nb. Doctor       - 2. Tester & Pliers\nc. Carpenter    - 3. Spanner & Wrench\nd. Mechanic     - 4. Saw & Hammer",
            "options": ["a-2, b-1, c-4, d-3", "a-3, b-1, c-4, d-2", "a-2, b-4, c-1, d-3", "a-4, b-1, c-2, d-3"],
            "correct_option": "a-2, b-1, c-4, d-3",
            "difficulty_level": "Hard",
            "solution_steps": "Electrician uses tester/pliers (2), doctor uses stethoscope (1), carpenter uses saw/hammer (4), mechanic uses spanner (3). Code is a-2, b-1, c-4, d-3.",
            "explanation_description": "Matching matrix."
        },
        {
            "question_text": "A plant is kept inside a sealed, dark cardboard box with no source of light but is watered daily. What will happen to the plant after a week?",
            "options": ["It will grow healthy and tall", "It will turn yellow and wilt due to lack of sunlight", "It will produce flowers quickly", "No change will happen"],
            "correct_option": "It will turn yellow and wilt due to lack of sunlight",
            "difficulty_level": "Hard",
            "solution_steps": "Without light, plants cannot perform photosynthesis, leading to loss of chlorophyll (yellowing) and death.",
            "explanation_description": "Plant survival conditions."
        },
        {
            "question_text": "An experiment shows a solid block sinking in a beaker of water. The block is then cut into two halves. What will happen if one half is put into the water beaker?",
            "options": ["It will float", "It will sink", "It will dissolve", "It will turn into vapor"],
            "correct_option": "It will sink",
            "difficulty_level": "Hard",
            "solution_steps": "Cutting the object does not change its density. If the whole object sinks, its half will also sink.",
            "explanation_description": "Density independence."
        },
        {
            "question_text": "Refer to the food components:\nW: Milk, Egg, Fish\nX: Potato, Rice, Sugar\nY: Orange, Spinach, Apple\nSelect the correct statement regarding W, X, and Y.",
            "options": ["W contains body-building nutrients and X contains energy-giving nutrients", "X helps in healing wounds and Y builds bones", "W protects us from diseases and Y provides instant energy", "All are protective foods"],
            "correct_option": "W contains body-building nutrients and X contains energy-giving nutrients",
            "difficulty_level": "Hard",
            "solution_steps": "W has proteins (body building), X has starch/carbs (energy giving), Y has vitamins (protective). Statement 1 is correct.",
            "explanation_description": "Nutrient groupings."
        },
        {
            "question_text": "Which of the following birds can swim in water, has webbed feet, and eats insects or plants? (Select the bird that matches these criteria)",
            "options": ["Woodpecker", "Eagle", "Duck", "Hummingbird"],
            "correct_option": "Duck",
            "difficulty_level": "Medium",
            "solution_steps": "Ducks have webbed feet and paddle in ponds, eating small fish, insects, and vegetation.",
            "explanation_description": "Locomotion and diet matching."
        },
        {
            "question_text": "Select the correct sequence of stages in the life cycle of a butterfly starting from the egg stage.",
            "options": ["Egg -> Pupa -> Larva -> Adult", "Egg -> Larva -> Pupa -> Adult", "Egg -> Adult -> Larva -> Pupa", "Egg -> Pupa -> Adult -> Larva"],
            "correct_option": "Egg -> Larva -> Pupa -> Adult",
            "difficulty_level": "Hard",
            "solution_steps": "Egg hatches into a caterpillar (larva), which forms a chrysalis (pupa), emerging as a butterfly (adult).",
            "explanation_description": "Life cycle sequencing."
        },
        {
            "question_text": "A shadow is formed on a screen. If the light source is moved closer to the opaque object, what happens to the size of the shadow?",
            "options": ["It becomes smaller", "It remains the same", "It becomes larger", "It disappears"],
            "correct_option": "It becomes larger",
            "difficulty_level": "Hard",
            "solution_steps": "Moving the light closer to the object blocks more light rays at a wider angle, casting a larger shadow.",
            "explanation_description": "Shadow size variation."
        },
        {
            "question_text": "Identify the constellation from the clues:\nClue 1: It is visible in the night sky.\nClue 2: It is shape like a hunter holding a shield and club.",
            "options": ["Ursa Major", "Cassiopeia", "Orion", "Leo"],
            "correct_option": "Orion",
            "difficulty_level": "Hard",
            "solution_steps": "Orion is known as the Hunter constellation and is marked by his distinctive belt of three bright stars.",
            "explanation_description": "Constellation identification."
        },
        {
            "question_text": "Select the option that correctly groups the organ systems with their main organs:\na. Circulatory system - 1. Stomach & Intestine\nb. Nervous system     - 2. Heart & Blood vessels\nc. Digestive system   - 3. Brain & Spinal cord",
            "options": ["a-2, b-3, c-1", "a-1, b-2, c-3", "a-3, b-2, c-1", "a-2, b-1, c-3"],
            "correct_option": "a-2, b-3, c-1",
            "difficulty_level": "Hard",
            "solution_steps": "Circulatory maps to Heart (2), Nervous maps to Brain (3), Digestive maps to Stomach (1). Sequence is a-2, b-3, c-1.",
            "explanation_description": "System mapping."
        },
        {
            "question_text": "An object sinks in water but floats on cooking oil. What can you conclude about its density?",
            "options": ["It is denser than water but less dense than oil", "It is denser than oil but less dense than water", "It is lighter than both", "It is heavier than both"],
            "correct_option": "It is denser than oil but less dense than water",
            "difficulty_level": "Hard",
            "solution_steps": "Sinking means density is higher. Floating means density is lower. The object is denser than oil, but less dense than water.",
            "explanation_description": "Comparative density deduction."
        },
        {
            "question_text": "Match the animal adaptions with their functions:\na. Polar bear fur - 1. Blending in green vegetation\nb. Chameleon      - 2. Flying in high altitude\nc. Eagle wings    - 3. Heat retention in icy cold",
            "options": ["a-3, b-1, c-2", "a-1, b-2, c-3", "a-2, b-1, c-3", "a-3, b-2, c-1"],
            "correct_option": "a-3, b-1, c-2",
            "difficulty_level": "Hard",
            "solution_steps": "Polar bear fur traps heat (3), chameleon blends into foliage (1), eagle wings support flight (2). Code is a-3, b-1, c-2.",
            "explanation_description": "Adaptation matching."
        },
        {
            "question_text": "Why do mountaineers carry oxygen cylinders while climbing high mountains?",
            "options": ["Oxygen is heavier at high altitudes", "The amount of oxygen in the air decreases at high altitudes", "Oxygen is needed to light fires on cold peaks", "There is no atmosphere on high peaks"],
            "correct_option": "The amount of oxygen in the air decreases at high altitudes",
            "difficulty_level": "Medium",
            "solution_steps": "The air density decreases with height, making it thinner and reducing available oxygen for breathing.",
            "explanation_description": "Altitude atmospheric change."
        },
        {
            "question_text": "Which of the following is correct about solid, liquid, and gaseous water?",
            "options": ["Ice has less energy than water vapor", "Water vapor has less energy than liquid water", "Heating liquid water turns it to ice", "Cooling water vapor turns it to steam"],
            "correct_option": "Ice has less energy than water vapor",
            "difficulty_level": "Hard",
            "solution_steps": "Molecules in gas (vapor) move fast and have high kinetic energy, while in solid (ice) they are locked and have low kinetic energy.",
            "explanation_description": "Molecular state energy."
        },
        {
            "question_text": "Select the correct statement about bird features:",
            "options": ["Down feathers keep the bird's body warm", "Flight feathers are fluffy and found near the skin", "Birds have heavy solid bones to withstand winds", "Woodpeckers have webbed feet to climb trees"],
            "correct_option": "Down feathers keep the bird's body warm",
            "difficulty_level": "Hard",
            "solution_steps": "Down feathers are small, soft, and trap heat. Flight feathers are large on wings. Bones are hollow (pneumatic). Woodpecker feet are zygodactyl.",
            "explanation_description": "Avian biology detail."
        },
        {
            "question_text": "What type of pollution would most likely result from dumping untreated plastic containers and chemicals directly into a pond?",
            "options": ["Air pollution", "Water and Soil pollution", "Noise pollution", "Only Air and Noise pollution"],
            "correct_option": "Water and Soil pollution",
            "difficulty_level": "Medium",
            "solution_steps": "Chemicals and plastics contaminate the water body, killing aquatic life, and leach into the surrounding soil.",
            "explanation_description": "Pollution effects."
        },
        {
            "question_text": "A child rubs a plastic comb against dry hair. The comb now attracts small pieces of paper. What force is responsible for this?",
            "options": ["Gravitational force", "Magnetic force", "Frictional force", "Electrostatic force"],
            "correct_option": "Electrostatic force",
            "difficulty_level": "Hard",
            "solution_steps": "Friction from rubbing creates a static electric charge on the comb, creating an electrostatic force that attracts paper.",
            "explanation_description": "Electrostatic force induction."
        },
        {
            "question_text": "Choose the correct sequence of water cycle processes:",
            "options": ["Condensation -> Evaporation -> Precipitation", "Evaporation -> Condensation -> Precipitation", "Precipitation -> Evaporation -> Condensation", "Condensation -> Precipitation -> Evaporation"],
            "correct_option": "Evaporation -> Condensation -> Precipitation",
            "difficulty_level": "Medium",
            "solution_steps": "Water boils/evaporates from seas into gas, condenses in cold air to form clouds, and falls as rain (precipitation).",
            "explanation_description": "Cycle sequencing."
        },
        {
            "question_text": "Which of these houses is portable, made of fabric/canvas, and used by campers?",
            "options": ["Stilt house", "Caravan", "Tent", "Bungalow"],
            "correct_option": "Tent",
            "difficulty_level": "Easy",
            "solution_steps": "Tents are temporary, collapsible shelters made of canvas or nylon used by travelers and soldiers.",
            "explanation_description": "Housing types."
        }
    ]

def populate_nso_quizzes_direct():
    print("Starting direct NSO Grade 3 quiz population...")
    
    sections = [
        {"name": "Logical Reasoning", "data": get_logical_reasoning()},
        {"name": "Science", "data": get_science()},
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
        existing_meta = supabase_db.table(quiz_table).select("id").eq("board", "CBSE").eq("grade", "Grade 3").eq("subject", "NSO Test").eq("chapter_or_topic", section_name).execute()
        if existing_meta.data:
            existing_id = existing_meta.data[0]["id"]
            print(f"Existing quiz found (ID: {existing_id}). Deleting old questions and quiz...")
            supabase_db.table(question_table).delete().eq(fk_field, existing_id).execute()
            supabase_db.table(quiz_table).delete().eq("id", existing_id).execute()
            
        # Create new quiz row
        quiz_metadata = {
            "board": "CBSE",
            "grade": "Grade 3",
            "subject": "NSO Test",
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
    populate_nso_quizzes_direct()
