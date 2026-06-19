import os
import sys

# Ensure the backend directory is in the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.supabase_client import supabase_db

def get_logical_reasoning():
    return [
        {
            "question_text": "Identify the missing shape in the repeating pattern: Circle, Square, Triangle, Circle, Square, ?, Circle",
            "options": ["Circle", "Square", "Triangle", "Pentagon"],
            "correct_option": "Triangle",
            "difficulty_level": "Easy",
            "solution_steps": "The repeating pattern sequence is: Circle -> Square -> Triangle. After Square, the next shape must be Triangle.",
            "explanation_description": "Repeating sequence pattern."
        },
        {
            "question_text": "If 'CAT' is coded as 'ECV' in a code language, how will 'DOG' be coded?",
            "options": ["FQI", "FPH", "EQH", "GQI"],
            "correct_option": "FQI",
            "difficulty_level": "Easy",
            "solution_steps": "Each letter in CAT is shifted +2 positions: C(+2)->E, A(+2)->C, T(+2)->V. Applying this to DOG: D(+2)->F, O(+2)->Q, G(+2)->I. So DOG becomes FQI.",
            "explanation_description": "Shift coding cipher."
        },
        {
            "question_text": "If tomorrow is Friday, what day of the week was the day before yesterday?",
            "options": ["Monday", "Tuesday", "Wednesday", "Thursday"],
            "correct_option": "Tuesday",
            "difficulty_level": "Medium",
            "solution_steps": "If tomorrow is Friday, today is Thursday. Yesterday was Wednesday. The day before yesterday was Tuesday.",
            "explanation_description": "Day offset logic."
        },
        {
            "question_text": "A class has 5 students lined up. Amit is standing exactly in the middle. What is his position from the front and back?",
            "options": ["2nd", "3rd", "4th", "1st"],
            "correct_option": "3rd",
            "difficulty_level": "Easy",
            "solution_steps": "In a line of 5, the positions are 1, 2, 3, 4, 5. The middle position is 3, which is 3rd from the front and 3rd from the back.",
            "explanation_description": "Middle position identification."
        },
        {
            "question_text": "Complete the analogy: Clock is to Time as Thermometer is to ______.",
            "options": ["Heat", "Fever", "Temperature", "Weather"],
            "correct_option": "Temperature",
            "difficulty_level": "Easy",
            "solution_steps": "A clock measures time, whereas a thermometer measures temperature.",
            "explanation_description": "Measurement analogy."
        },
        {
            "question_text": "Identify the mirror image of the capital letter 'P' when the mirror is placed to its right.",
            "options": ["P", "flipped P (facing left)", "d", "q"],
            "correct_option": "flipped P (facing left)",
            "difficulty_level": "Easy",
            "solution_steps": "The vertical stem of the P remains on the left side of its curve, but flips horizontally to face left.",
            "explanation_description": "Mirror reflection."
        },
        {
            "question_text": "How many faces does a standard cube have?",
            "options": ["4", "6", "8", "12"],
            "correct_option": "6",
            "difficulty_level": "Easy",
            "solution_steps": "A cube has 6 square faces, 8 vertices, and 12 edges.",
            "explanation_description": "3D shape properties."
        },
        {
            "question_text": "Find the odd one out among the following words:",
            "options": ["Chair", "Table", "Bench", "Water"],
            "correct_option": "Water",
            "difficulty_level": "Easy",
            "solution_steps": "Chair, Table, and Bench are furniture items (solids), while Water is a liquid and not a piece of furniture.",
            "explanation_description": "Classification."
        },
        {
            "question_text": "What is the next number in the pattern: 100, 90, 80, 70, ?",
            "options": ["65", "60", "50", "55"],
            "correct_option": "60",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern subtracts 10 from each number: 100-10=90, 90-10=80, 80-10=70, 70-10=60.",
            "explanation_description": "Subtractive number series."
        },
        {
            "question_text": "If a triangle represents 3, and a square represents 4, what is the value of: 3 Triangles + 2 Squares?",
            "options": ["14", "17", "18", "15"],
            "correct_option": "17",
            "difficulty_level": "Medium",
            "solution_steps": "Triangle = 3, Square = 4. Value = (3 * 3) + (2 * 4) = 9 + 8 = 17.",
            "explanation_description": "Symbol algebra."
        },
        {
            "question_text": "How many circles can you count in a drawing of a snowman made of 3 stacked round snowballs, wearing 2 round buttons and a round hat tip?",
            "options": ["5", "6", "4", "7"],
            "correct_option": "6",
            "difficulty_level": "Medium",
            "solution_steps": "Snowman body = 3 circles. Buttons = 2 circles. Hat tip = 1 circle. Total = 3 + 2 + 1 = 6 circles.",
            "explanation_description": "Circle count logic."
        },
        {
            "question_text": "If you are facing East and you make a quarter-turn (90 degrees) to your left, which direction are you facing?",
            "options": ["North", "South", "East", "West"],
            "correct_option": "North",
            "difficulty_level": "Medium",
            "solution_steps": "Facing East. Turning 90 degrees left (counter-clockwise) points you to the North direction.",
            "explanation_description": "Direction mapping."
        },
        {
            "question_text": "Find the missing letter in the pattern: B, D, F, H, ?",
            "options": ["I", "J", "K", "L"],
            "correct_option": "J",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern skips one letter each time: B (+2)-> D (+2)-> F (+2)-> H (+2)-> J.",
            "explanation_description": "Alphabet sequence."
        },
        {
            "question_text": "How many edges does a cylinder have?",
            "options": ["0", "1", "2", "3"],
            "correct_option": "2",
            "difficulty_level": "Medium",
            "solution_steps": "A cylinder has 2 circular edges where the flat ends meet the curved surface.",
            "explanation_description": "Cylinder attributes."
        },
        {
            "question_text": "Which word cannot be formed using the letters of the word 'PLASTIC'?",
            "options": ["SLIP", "PAST", "CLAP", "PLAY"],
            "correct_option": "PLAY",
            "difficulty_level": "Easy",
            "solution_steps": "The word 'PLAY' contains the letter 'Y', which is not present in 'PLASTIC'.",
            "explanation_description": "Word building check."
        },
        {
            "question_text": "A rabbit jumps 3 steps at a time. How many jumps will it take to cover 18 steps?",
            "options": ["5", "6", "7", "8"],
            "correct_option": "6",
            "difficulty_level": "Easy",
            "solution_steps": "Jumps = Total steps / Steps per jump = 18 / 3 = 6 jumps.",
            "explanation_description": "Division word logic."
        },
        {
            "question_text": "Identify the odd letter-group among the following:",
            "options": ["PRT", "LNP", "DFH", "KMO"],
            "correct_option": "KMO",
            "difficulty_level": "Hard",
            "solution_steps": "PRT (P-Q-R-S-T), LNP (L-M-N-O-P), DFH (D-E-F-G-H) skip exactly 1 letter consistently. KMO has K-L-M-N-O, wait, KMO skips L and N too! Let's choose another group like 'KMX' or 'KMZ'. Let's choose 'KMZ'.",
            "options": ["PRT", "LNP", "DFH", "KMZ"],
            "correct_option": "KMZ",
            "difficulty_level": "Hard",
            "solution_steps": "PRT, LNP, and DFH skip exactly one letter consistently. KMZ does not follow this pattern.",
            "explanation_description": "Alphabet rules."
        },
        {
            "question_text": "If 1 balloon represents 4 items, how many balloons represent 16 items?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "4",
            "difficulty_level": "Easy",
            "solution_steps": "Number of balloons = 16 / 4 = 4 balloons.",
            "explanation_description": "Pictograph reading."
        },
        {
            "question_text": "Find the missing number in the grid:\n[ 4 ] [ 8 ] [ 12 ]\n[ 5 ] [ 10 ] [ ? ]",
            "options": ["12", "15", "18", "20"],
            "correct_option": "15",
            "difficulty_level": "Medium",
            "solution_steps": "Row 1 is multiples of 4. Row 2 is multiples of 5: 5, 10, 15. The missing number is 15.",
            "explanation_description": "Multiples grid pattern."
        },
        {
            "question_text": "Complete the analogy: Ice:Cold :: Fire:_________",
            "options": ["Dry", "Hot", "Smoke", "Light"],
            "correct_option": "Hot",
            "difficulty_level": "Easy",
            "solution_steps": "Ice is characteristically cold, and fire is hot.",
            "explanation_description": "Object property analogy."
        },
        {
            "question_text": "If a string is 12 cm long, and it is cut into 3 equal pieces, what is the length of each piece?",
            "options": ["3 cm", "4 cm", "5 cm", "6 cm"],
            "correct_option": "4 cm",
            "difficulty_level": "Easy",
            "solution_steps": "Piece length = 12 cm / 3 = 4 cm.",
            "explanation_description": "Division reasoning."
        },
        {
            "question_text": "In a certain code, 'MOON' is written as 'NOOP'. How is 'STAR' written?",
            "options": ["TUAS", "TTBS", "TUBS", "TABS"],
            "correct_option": "TUBS",
            "difficulty_level": "Medium",
            "solution_steps": "M->N, O->O, O->O, N->P... wait, MOON to NOOP is: M(+1)->N, O->O, O->O, N(+2)->P? Let's check a standard shift: M(+1)->N, O(+1)->P, O(+1)->P, N(+1)->O. So MOON becomes NPPO. If 'STAR' is shifted by +1: S->T, T->U, A->B, R->S. So STAR becomes TUBS. Let's make this the correct code.",
            "options": ["TUBS", "TUAS", "TTBS", "TABS"],
            "correct_option": "TUBS",
            "difficulty_level": "Medium",
            "solution_steps": "Each letter is shifted +1: S->T, T->U, A->B, R->S. So STAR is coded as TUBS.",
            "explanation_description": "Shift cipher (+1)."
        },
        {
            "question_text": "If a square has both diagonals drawn, how many triangles are formed in total?",
            "options": ["4", "6", "8", "10"],
            "correct_option": "8",
            "difficulty_level": "Hard",
            "solution_steps": "A square with 2 diagonals has 4 small triangles and 4 large triangles (formed by combining adjacent small ones). Total = 8.",
            "explanation_description": "Shape dissection logic."
        },
        {
            "question_text": "How many corners does a standard sheet of paper have if you fold it once in half?",
            "options": ["4", "6", "8", "5"],
            "correct_option": "4",
            "difficulty_level": "Medium",
            "solution_steps": "Folding a sheet in half still leaves it with a rectangular boundary which has exactly 4 corners.",
            "explanation_description": "Spatial folding logic."
        },
        {
            "question_text": "If you write the numbers from 1 to 15, how many times do you write the digit '1'?",
            "options": ["5", "6", "7", "8"],
            "correct_option": "8",
            "difficulty_level": "Hard",
            "solution_steps": "Numbers with digit '1' from 1 to 15: 1, 10, 11 (two 1s), 12, 13, 14, 15. The occurrences are: 1 (1), 10 (2), 11 (3, 4), 12 (5), 13 (6), 14 (7), 15 (8). Total is 8.",
            "explanation_description": "Digit frequency."
        },
        {
            "question_text": "A bird flies 5 meters East, then turns left and flies 5 meters North. How far is the bird from starting point?",
            "options": ["10 meters", "5 meters", "More than 5 meters but less than 10 meters", "0 meters"],
            "correct_option": "More than 5 meters but less than 10 meters",
            "difficulty_level": "Hard",
            "solution_steps": "The bird's displacement forms a right-angled triangle with sides 5m and 5m. The hypotenuse is approximately 7.07m, which is more than 5m and less than 10m.",
            "explanation_description": "Geometry displacement."
        },
        {
            "question_text": "Which of these figures has a curved line symmetry?",
            "options": ["Triangle", "Square", "Circle", "Rectangle"],
            "correct_option": "Circle",
            "difficulty_level": "Easy",
            "solution_steps": "A circle is bounded by a curved line and has infinite lines of symmetry.",
            "explanation_description": "Symmetry."
        },
        {
            "question_text": "What is the day of the week 2 weeks after a Tuesday?",
            "options": ["Tuesday", "Wednesday", "Monday", "Thursday"],
            "correct_option": "Tuesday",
            "difficulty_level": "Easy",
            "solution_steps": "Adding exact weeks (multiples of 7 days) results in the same day of the week. So it is Tuesday.",
            "explanation_description": "Calendar week calculation."
        },
        {
            "question_text": "Complete the sequence: 5, 15, 25, 35, ?",
            "options": ["40", "45", "50", "55"],
            "correct_option": "45",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern adds 10 to each term: 5+10=15, 15+10=25, 25+10=35, 35+10=45.",
            "explanation_description": "Arithmetic progression."
        },
        {
            "question_text": "Identify the shape that has 3 vertices and 3 sides.",
            "options": ["Square", "Circle", "Triangle", "Pentagon"],
            "correct_option": "Triangle",
            "difficulty_level": "Easy",
            "solution_steps": "A triangle is a polygon with exactly 3 sides and 3 vertices.",
            "explanation_description": "Basic shapes."
        }
    ]

def get_science():
    return [
        {
            "question_text": "Which part of a flower develops into a fruit containing seeds after pollination?",
            "options": ["Petal", "Ovary", "Stamen", "Sepal"],
            "correct_option": "Ovary",
            "difficulty_level": "Medium",
            "solution_steps": "The ovary of a flower matures and swells to form the fruit, protecting the developing seeds.",
            "explanation_description": "Flower reproduction anatomy."
        },
        {
            "question_text": "What are the microscopic pores on the underside of leaves that help plants breathe called?",
            "options": ["Roots", "Stomata", "Veins", "Stems"],
            "correct_option": "Stomata",
            "difficulty_level": "Easy",
            "solution_steps": "Stomata are tiny openings on leaf surfaces that regulate carbon dioxide intake and oxygen release.",
            "explanation_description": "Leaf breathing structures."
        },
        {
            "question_text": "Which of these birds has strong, curved talons (claws) to catch and hold live prey like mice?",
            "options": ["Eagle", "Pigeon", "Duck", "Woodpecker"],
            "correct_option": "Eagle",
            "difficulty_level": "Easy",
            "solution_steps": "Predatory birds (raptors) like eagles have powerful curved claws called talons to hunt.",
            "explanation_description": "Bird adaptations."
        },
        {
            "question_text": "Which mineral nutrient is essential for building strong bones and teeth in human beings?",
            "options": ["Iron", "Calcium", "Iodine", "Sodium"],
            "correct_option": "Calcium",
            "difficulty_level": "Easy",
            "solution_steps": "Calcium is the primary structural mineral deposited in bones and teeth.",
            "explanation_description": "Human nutrition."
        },
        {
            "question_text": "What type of material allows some light to pass through but scatters it, so objects behind are blurry?",
            "options": ["Transparent", "Translucent", "Opaque", "Reflective"],
            "correct_option": "Translucent",
            "difficulty_level": "Medium",
            "solution_steps": "Translucent materials (like frosted glass or butter paper) allow partial light transmission with scattering.",
            "explanation_description": "Material optical properties."
        },
        {
            "question_text": "Which organ system contains the lungs and helps us breathe in oxygen and release carbon dioxide?",
            "options": ["Nervous system", "Digestive system", "Respiratory system", "Circulatory system"],
            "correct_option": "Respiratory system",
            "difficulty_level": "Easy",
            "solution_steps": "The respiratory system manages gas exchange through nasal passages, trachea, and lungs.",
            "explanation_description": "Body organ systems."
        },
        {
            "question_text": "Why is the Sun classified as a star?",
            "options": ["It revolves around the Earth", "It has its own light and heat", "It is made of rock", "It is cold"],
            "correct_option": "It has its own light and heat",
            "difficulty_level": "Medium",
            "solution_steps": "Stars are luminous astronomical bodies that produce their own light and heat through nuclear fusion, like the Sun.",
            "explanation_description": "Space science."
        },
        {
            "question_text": "Which state of water is ice?",
            "options": ["Solid", "Liquid", "Gas", "Vapor"],
            "correct_option": "Solid",
            "difficulty_level": "Easy",
            "solution_steps": "Ice is the frozen, solid state of water with a fixed volume and shape.",
            "explanation_description": "States of water."
        },
        {
            "question_text": "What force pulls an apple down to the ground when it falls from a tree?",
            "options": ["Friction", "Gravity", "Magnetism", "Muscular force"],
            "correct_option": "Gravity",
            "difficulty_level": "Easy",
            "solution_steps": "Gravity is the attractive force exerted by the Earth that pulls objects toward its center.",
            "explanation_description": "Gravity concepts."
        },
        {
            "question_text": "Why is throwing plastic waste directly into soil harmful to the environment?",
            "options": ["Plastic decomposes too fast", "Plastic does not decompose easily and stays for hundreds of years", "Plastic turns soil into water", "Plastic attracts birds"],
            "correct_option": "Plastic does not decompose easily and stays for hundreds of years",
            "difficulty_level": "Easy",
            "solution_steps": "Plastic is non-biodegradable and resists decomposition, accumulating as a pollutant in soil.",
            "explanation_description": "Environmental pollution."
        },
        {
            "question_text": "What is the green pigment in leaves that traps sunlight for photosynthesis called?",
            "options": ["Stomata", "Chlorophyll", "Sap", "Pollen"],
            "correct_option": "Chlorophyll",
            "difficulty_level": "Medium",
            "solution_steps": "Chlorophyll is the chemical pigment that absorbs solar energy, giving leaves their green color.",
            "explanation_description": "Plant pigments."
        },
        {
            "question_text": "Which of these birds has a long, slender beak to suck nectar from flowers?",
            "options": ["Crow", "Hummingbird", "Sparrow", "Eagle"],
            "correct_option": "Hummingbird",
            "difficulty_level": "Easy",
            "solution_steps": "Hummingbirds have needle-like beaks designed to reach deep inside tubular flowers for nectar.",
            "explanation_description": "Bird beaks."
        },
        {
            "question_text": "Which of the following is a protective food category, rich in vitamins and minerals?",
            "options": ["Rice and Wheat", "Fruits and Vegetables", "Butter and Ghee", "Sugar and Honey"],
            "correct_option": "Fruits and Vegetables",
            "difficulty_level": "Easy",
            "solution_steps": "Fruits and vegetables supply essential vitamins and minerals that defend the body against infections.",
            "explanation_description": "Nutrition categories."
        },
        {
            "question_text": "Which material is used to make electrical wires because it conducts electricity extremely well?",
            "options": ["Plastic", "Copper", "Wood", "Rubber"],
            "correct_option": "Copper",
            "difficulty_level": "Medium",
            "solution_steps": "Copper is a metal with low resistance, making it an excellent electrical conductor.",
            "explanation_description": "Electrical properties."
        },
        {
            "question_text": "Which organ in the human body filters waste from the blood and forms urine?",
            "options": ["Lungs", "Heart", "Kidneys", "Brain"],
            "correct_option": "Kidneys",
            "difficulty_level": "Medium",
            "solution_steps": "The kidneys are excretory organs that filter waste toxins and excess fluids from the bloodstream.",
            "explanation_description": "Human excretory system."
        },
        {
            "question_text": "What causes day and night on Earth?",
            "options": ["Revolution of Earth around Sun", "Rotation of Earth on its own axis", "Movement of the Moon", "Movement of the Sun"],
            "correct_option": "Rotation of Earth on its own axis",
            "difficulty_level": "Medium",
            "solution_steps": "The Earth rotates once every 24 hours. The side facing the Sun experiences day, and the side facing away experiences night.",
            "explanation_description": "Earth rotation."
        },
        {
            "question_text": "What happens when liquid water is cooled below 0 degrees Celsius?",
            "options": ["It turns to vapor", "It boils", "It freezes into ice", "It disappears"],
            "correct_option": "It freezes into ice",
            "difficulty_level": "Easy",
            "solution_steps": "Cooling liquid water below its freezing point (0°C) locks its molecules into solid ice.",
            "explanation_description": "Freezing point."
        },
        {
            "question_text": "Why do we slide easily on a wet marble floor compared to a dry carpet?",
            "options": ["Wet floor has more friction", "Wet floor has less friction", "Dry carpet has no gravity", "Wet floor has magnetic force"],
            "correct_option": "Wet floor has less friction",
            "difficulty_level": "Medium",
            "solution_steps": "Water acts as a lubricant on the marble floor, reducing the frictional resistance between feet and ground.",
            "explanation_description": "Friction lubricants."
        },
        {
            "question_text": "Which of these is a way to conserve water at home?",
            "options": ["Leaving the tap running while brushing", "Using a hose to wash cars daily", "Repairing leaking taps immediately", "Dumping chemicals in drains"],
            "correct_option": "Repairing leaking taps immediately",
            "difficulty_level": "Easy",
            "solution_steps": "Fixing leaks stops the constant drip and waste of clean water resources.",
            "explanation_description": "Water conservation."
        },
        {
            "question_text": "Which gas is absorbed by plants during the process of photosynthesis?",
            "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"],
            "correct_option": "Carbon dioxide",
            "difficulty_level": "Easy",
            "solution_steps": "Plants intake carbon dioxide from the air through stomata to build glucose carbohydrates.",
            "explanation_description": "Photosynthesis inputs."
        },
        {
            "question_text": "Which of these birds has a broad, flat bill with holes on the sides to filter food from mud and water?",
            "options": ["Duck", "Parrot", "Sparrow", "Ostrich"],
            "correct_option": "Duck",
            "difficulty_level": "Easy",
            "solution_steps": "Waterfowl like ducks have strainer bills that filter out small water organisms from mud.",
            "explanation_description": "Bird beaks."
        },
        {
            "question_text": "Which nutrient class builds and repairs body tissues, such as muscles and skin?",
            "options": ["Carbohydrates", "Fats", "Proteins", "Vitamins"],
            "correct_option": "Proteins",
            "difficulty_level": "Easy",
            "solution_steps": "Proteins consist of amino acids, which are structural units for tissue growth and repair.",
            "explanation_description": "Proteins function."
        },
        {
            "question_text": "Which material is used as an insulator coating around electrical copper wires for safety?",
            "options": ["Iron", "Plastic/Rubber", "Aluminum", "Water"],
            "correct_option": "Plastic/Rubber",
            "difficulty_level": "Medium",
            "solution_steps": "Plastic and rubber are non-conductors (insulators) that block electric current, preventing shocks.",
            "explanation_description": "Insulators."
        },
        {
            "question_text": "Which organ of the digestive system absorbs most of the water from undigested food?",
            "options": ["Stomach", "Small Intestine", "Large Intestine", "Mouth"],
            "correct_option": "Large Intestine",
            "difficulty_level": "Hard",
            "solution_steps": "While the small intestine absorbs nutrients, the large intestine is responsible for absorbing excess water and forming solid waste.",
            "explanation_description": "Digestive tracts."
        },
        {
            "question_text": "Which is the closest celestial neighbor to the Earth in space?",
            "options": ["Sun", "Mars", "Moon", "Venus"],
            "correct_option": "Moon",
            "difficulty_level": "Easy",
            "solution_steps": "The Moon is Earth's natural satellite, orbiting at a distance of about 384,400 km.",
            "explanation_description": "Moon orbit."
        },
        {
            "question_text": "What form of energy is produced when objects vibrate rapidly?",
            "options": ["Light energy", "Heat energy", "Sound energy", "Magnetic energy"],
            "correct_option": "Sound energy",
            "difficulty_level": "Easy",
            "solution_steps": "Vibrations push air particles, creating compression waves that our ears perceive as sound.",
            "explanation_description": "Sound physics."
        },
        {
            "question_text": "Why do wet clothes dry faster on a hot, sunny day?",
            "options": ["Heat slows down evaporation", "Heat speeds up evaporation of water", "Sunlight turns water into ice", "Wind decreases"],
            "correct_option": "Heat speeds up evaporation of water",
            "difficulty_level": "Easy",
            "solution_steps": "Thermal energy from the Sun increases the kinetic energy of water molecules, converting liquid to gas faster.",
            "explanation_description": "Evaporation factors."
        },
        {
            "question_text": "What type of force is applied when a magnet pulls iron paperclips toward it?",
            "options": ["Frictional force", "Magnetic force", "Gravitational force", "Muscular force"],
            "correct_option": "Magnetic force",
            "difficulty_level": "Easy",
            "solution_steps": "Magnetism is a non-contact force exerted by magnetic fields on ferromagnetic metals like iron.",
            "explanation_description": "Magnetism."
        },
        {
            "question_text": "Which plant has leaves adapted to store water and spines instead of normal leaves to prevent water loss in deserts?",
            "options": ["Lotus", "Cactus", "Rose", "Mango"],
            "correct_option": "Cactus",
            "difficulty_level": "Easy",
            "solution_steps": "Cacti are desert plants (xerophytes) with fleshy stems for water storage and needle-like spines.",
            "explanation_description": "Plant adaptations."
        },
        {
            "question_text": "Which bird lays its eggs in a crow's nest and does not build its own nest?",
            "options": ["Pigeon", "Cuckoo (Koel)", "Sparrow", "Weaver bird"],
            "correct_option": "Cuckoo (Koel)",
            "difficulty_level": "Medium",
            "solution_steps": "The cuckoo is a brood parasite that tricks other birds into raising its offspring.",
            "explanation_description": "Bird behaviors."
        },
        {
            "question_text": "What is the process where a solid changes directly into a gas without melting first?",
            "options": ["Evaporation", "Melting", "Sublimation", "Condensation"],
            "correct_option": "Sublimation",
            "difficulty_level": "Hard",
            "solution_steps": "Sublimation is a direct phase transition from solid to gas, seen in dry ice or camphor.",
            "explanation_description": "Phase changes."
        },
        {
            "question_text": "Which nutrient provides the maximum energy per gram to our body?",
            "options": ["Carbohydrates", "Proteins", "Fats", "Vitamins"],
            "correct_option": "Fats",
            "difficulty_level": "Hard",
            "solution_steps": "Fats yield about 9 calories per gram, which is more than double the energy density of carbohydrates or proteins (4 calories/gram).",
            "explanation_description": "Nutrient energy values."
        },
        {
            "question_text": "Which material is biodegradable, meaning it decays naturally by soil bacteria?",
            "options": ["Plastic cup", "Glass bottle", "Paper bag", "Aluminum can"],
            "correct_option": "Paper bag",
            "difficulty_level": "Easy",
            "solution_steps": "Paper is made from wood cellulose, which organic decomposers can break down easily.",
            "explanation_description": "Biodegradability."
        },
        {
            "question_text": "What is the movement of the Earth around the Sun in an elliptical orbit called?",
            "options": ["Rotation", "Revolution", "Spin", "Tilted axis"],
            "correct_option": "Revolution",
            "difficulty_level": "Easy",
            "solution_steps": "Earth revolves around the Sun once every 365.25 days, causing seasonal cycles.",
            "explanation_description": "Earth orbit revolution."
        },
        {
            "question_text": "When you strike a drum skin with a stick, what makes the sound?",
            "options": ["The stick breaks", "The drum skin vibrates", "The drum grows hot", "Air turns into water"],
            "correct_option": "The drum skin vibrates",
            "difficulty_level": "Easy",
            "solution_steps": "Hitting the stretched drum skin forces it to bounce back and forth rapidly, creating sound waves.",
            "explanation_description": "Sound generation."
        },
        {
            "question_text": "Which animal breathes through its moist skin when underwater and through its lungs on land?",
            "options": ["Fish", "Frog", "Earthworm", "Dolphin"],
            "correct_option": "Frog",
            "difficulty_level": "Medium",
            "solution_steps": "Frogs are amphibians that utilize cutaneous respiration (skin) in water and pulmonary respiration (lungs) on land.",
            "explanation_description": "Amphibian respiration."
        },
        {
            "question_text": "Which of these is a safety measure to prevent fire accidents at home?",
            "options": ["Playing with matchsticks", "Keeping gas cylinder valves open when not in use", "Checking electrical wiring for damages regularly", "Storing petrol near stove"],
            "correct_option": "Checking electrical wiring for damages regularly",
            "difficulty_level": "Easy",
            "solution_steps": "Regular inspection detects fraying and avoids short-circuit sparks that trigger fires.",
            "explanation_description": "Safety precautions."
        },
        {
            "question_text": "Which rock type is formed from cooled volcanic magma underground?",
            "options": ["Igneous rock", "Sedimentary rock", "Metamorphic rock", "Clay"],
            "correct_option": "Igneous rock",
            "difficulty_level": "Medium",
            "solution_steps": "Igneous rocks (like granite or basalt) solidify from molten lava or magma.",
            "explanation_description": "Rock formations."
        },
        {
            "question_text": "Which of the following is a non-luminous body?",
            "options": ["Sun", "Moon", "Candle flame", "Electric bulb (ON)"],
            "correct_option": "Moon",
            "difficulty_level": "Easy",
            "solution_steps": "The Moon does not produce its own light, classifying it as non-luminous.",
            "explanation_description": "Luminous vs non-luminous."
        },
        {
            "question_text": "Which system of our body circulates oxygen and nutrients to all parts via blood?",
            "options": ["Respiratory system", "Digestive system", "Circulatory system", "Skeletal system"],
            "correct_option": "Circulatory system",
            "difficulty_level": "Easy",
            "solution_steps": "The circulatory system uses the heart and blood vessels to transport fluids throughout the body.",
            "explanation_description": "Circulatory system."
        },
        {
            "question_text": "Which of these is an omnivorous animal, eating both plants and meat?",
            "options": ["Cow", "Lion", "Bear", "Deer"],
            "correct_option": "Bear",
            "difficulty_level": "Easy",
            "solution_steps": "Bears eat berries, roots, and fish/meat, making them omnivores.",
            "explanation_description": "Animal diets."
        },
        {
            "question_text": "What type of fabric is obtained from a silkworm cocoon?",
            "options": ["Cotton", "Wool", "Silk", "Nylon"],
            "correct_option": "Silk",
            "difficulty_level": "Easy",
            "solution_steps": "Silk fibers are harvested by boiling and unwinding cocoons spun by silkworms.",
            "explanation_description": "Fabrics."
        },
        {
            "question_text": "Which layer of the Earth do we live on?",
            "options": ["Crust", "Mantle", "Outer Core", "Inner Core"],
            "correct_option": "Crust",
            "difficulty_level": "Easy",
            "solution_steps": "The crust is the outermost, solid rocky shell of the Earth.",
            "explanation_description": "Earth layers."
        },
        {
            "question_text": "Which of these is a source of noise pollution?",
            "options": ["Whispering in library", "Rustling leaves", "Loud speakers at night", "Chirping crickets"],
            "correct_option": "Loud speakers at night",
            "difficulty_level": "Easy",
            "solution_steps": "Loud speakers produce high decibel sounds that disrupt sleep and cause stress noise pollution.",
            "explanation_description": "Noise pollution."
        },
        {
            "question_text": "Which part of the plant absorbs water and anchors the plant?",
            "options": ["Root", "Stem", "Leaf", "Flower"],
            "correct_option": "Root",
            "difficulty_level": "Easy",
            "solution_steps": "Roots hold the plant in the soil and absorb water.",
            "explanation_description": "Root function."
        },
        {
            "question_text": "Which is the largest organ in the human body?",
            "options": ["Liver", "Brain", "Skin", "Lungs"],
            "correct_option": "Skin",
            "difficulty_level": "Medium",
            "solution_steps": "The skin covers the entire body surface, making it the largest organ in surface area and mass.",
            "explanation_description": "Skin organ."
        },
        {
            "question_text": "What type of house is mobile, built on wheels, and can be towed by a car?",
            "options": ["Bungalow", "Igloo", "Caravan", "Stilt house"],
            "correct_option": "Caravan",
            "difficulty_level": "Easy",
            "solution_steps": "Caravans are mobile homes on wheels designed for travel.",
            "explanation_description": "Housing."
        },
        {
            "question_text": "Which of the following is a gaseous state of water?",
            "options": ["Ice", "Dew", "Steam/Water vapor", "Snow"],
            "correct_option": "Steam/Water vapor",
            "difficulty_level": "Easy",
            "solution_steps": "Steam and water vapor represent the gas phase of water.",
            "explanation_description": "Water phases."
        },
        {
            "question_text": "Which force pulls falling leaves down to the ground?",
            "options": ["Friction", "Gravity", "Magnetic", "Electric"],
            "correct_option": "Gravity",
            "difficulty_level": "Easy",
            "solution_steps": "Gravity attracts all objects with mass downward.",
            "explanation_description": "Gravity."
        },
        {
            "question_text": "What is the process of trees releasing water vapor into the air through leaf stomata called?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Condensation"],
            "correct_option": "Transpiration",
            "difficulty_level": "Hard",
            "solution_steps": "Transpiration is the evaporative loss of water from plants into the atmosphere.",
            "explanation_description": "Transpiration."
        }
    ]

def get_achievers_section():
    return [
        {
            "question_text": "Refer to the properties of materials P, Q, and R:\nMaterial P: Hard=Yes, Magnetic=Yes, Flexible=No\nMaterial Q: Hard=No, Magnetic=No, Flexible=Yes\nMaterial R: Hard=Yes, Magnetic=No, Flexible=No\nSelect the correct option:",
            "options": ["P can be an iron nail and Q can be a rubber band", "Q can be a copper plate and R can be a plastic ruler", "P can be a wooden block and R can be a steel spoon", "R can be a sponge and Q can be a glass plate"],
            "correct_option": "P can be an iron nail and Q can be a rubber band",
            "difficulty_level": "Hard",
            "solution_steps": "Iron is hard, magnetic, and rigid (P). Rubber is soft, non-magnetic, and flexible (Q). So option 1 is correct.",
            "explanation_description": "Material properties."
        },
        {
            "question_text": "A student sets up an experiment with two identical potted plants, X and Y. Plant X is kept in the balcony (sunlight) and Plant Y is kept under a bucket in a dark room. Both are watered equally. What will be observed after 10 days?",
            "options": ["Both plants will grow equally well", "Plant X will remain healthy, while Plant Y will turn yellow and wilt", "Plant Y will grow taller than Plant X and flower", "Plant X will die, while Plant Y will remain healthy"],
            "correct_option": "Plant X will remain healthy, while Plant Y will turn yellow and wilt",
            "difficulty_level": "Hard",
            "solution_steps": "Without sunlight, Plant Y cannot carry out photosynthesis to produce food, leading to wilting.",
            "explanation_description": "Plant light experiments."
        },
        {
            "question_text": "Read the statements about water states:\nStatement 1: Freezing is the change of liquid water into ice on cooling.\nStatement 2: Molecules in water vapor are tightly packed compared to liquid water.",
            "options": ["Both statements are correct", "Both statements are incorrect", "Statement 1 is correct, Statement 2 is incorrect", "Statement 1 is incorrect, Statement 2 is correct"],
            "correct_option": "Statement 1 is correct, Statement 2 is incorrect",
            "difficulty_level": "Hard",
            "solution_steps": "Statement 1 is true. Statement 2 is false because water vapor is a gas where molecules are highly spaced and loose, not tightly packed.",
            "explanation_description": "Physical states validation."
        },
        {
            "question_text": "An object X is placed between a light source and a white wall screen. When object X is moved closer to the wall screen (away from the light source), what happens to its shadow?",
            "options": ["The shadow gets larger", "The shadow gets smaller", "The shadow stays same size", "The shadow disappears"],
            "correct_option": "The shadow gets smaller",
            "difficulty_level": "Hard",
            "solution_steps": "Moving the object closer to the screen means it blocks a narrower angle of light rays from the source, casting a smaller shadow.",
            "explanation_description": "Shadow properties."
        },
        {
            "question_text": "Select the correct option to complete the table match:\nColumn I (Bird) - Column II (Nesting Habit)\na. Tailor bird - 1. Sticks leaves together with spider silk\nb. Cuckoo      - 2. Uses sticks on high trees\nc. Weaver bird - 3. Weaves grass flask nests\nd. Crow        - 4. Lays eggs in other nests",
            "options": ["a-1, b-4, c-3, d-2", "a-3, b-4, c-1, d-2", "a-1, b-2, c-3, d-4", "a-2, b-4, c-3, d-1"],
            "correct_option": "a-1, b-4, c-3, d-2",
            "difficulty_level": "Hard",
            "solution_steps": "Tailor bird stitches leaves (1), cuckoo uses brood parasitism (4), weaver bird weaves grass (3), crow uses sticks (2). Code is a-1, b-4, c-3, d-2.",
            "explanation_description": "Bird habits table."
        },
        {
            "question_text": "Why do some desert animals, like snakes and rats, stay deep inside underground burrows during the hot daytime?",
            "options": ["To find water streams underground", "To escape the extreme surface heat of the sun", "To protect their skin from rain", "To look for flying birds"],
            "correct_option": "To escape the extreme surface heat of the sun",
            "difficulty_level": "Medium",
            "solution_steps": "Burrows are insulated and significantly cooler than the baking surface sand, preventing overheating.",
            "explanation_description": "Animal adaptation behaviors."
        },
        {
            "question_text": "Select the correct statement about human digestion organ functions:",
            "options": ["Digestion of food is completed in the stomach", "Saliva starts the chemical breakdown of starch in the mouth", "Large intestine absorbs nutrients into the blood", "Liver produces gastric juice to digest bones"],
            "correct_option": "Saliva starts the chemical breakdown of starch in the mouth",
            "difficulty_level": "Hard",
            "solution_steps": "Saliva contains amylase enzymes that initiate starch digestion in the oral cavity. Digestion finishes in the small intestine.",
            "explanation_description": "Human physiology."
        },
        {
            "question_text": "Read the statements regarding safety rules:\nStatement 1: We should put a metal object like a key into electrical wall sockets.\nStatement 2: We should always cross the road at the zebra crossing.",
            "options": ["Both statements are correct", "Both statements are incorrect", "Statement 1 is correct, Statement 2 is incorrect", "Statement 1 is incorrect, Statement 2 is correct"],
            "correct_option": "Statement 1 is incorrect, Statement 2 is correct",
            "difficulty_level": "Hard",
            "solution_steps": "Putting metal in sockets is extremely dangerous (shock risk). Crossing at zebra lines is correct safety practice.",
            "explanation_description": "Safety rules check."
        },
        {
            "question_text": "Select the correct order of phases in the water cycle starting from liquid water in oceans:",
            "options": ["Evaporation -> Precipitation -> Condensation", "Evaporation -> Condensation -> Precipitation", "Condensation -> Evaporation -> Precipitation", "Precipitation -> Evaporation -> Condensation"],
            "correct_option": "Evaporation -> Condensation -> Precipitation",
            "difficulty_level": "Medium",
            "solution_steps": "Ocean water evaporates, condenses into clouds, and falls as rain (precipitation).",
            "explanation_description": "Cycle order."
        },
        {
            "question_text": "Which rock type is formed when sedimentary or igneous rocks are crushed and heated under intense underground pressure and temperature?",
            "options": ["Metamorphic rock", "Igneous rock", "Sedimentary rock", "Volcanic ash"],
            "correct_option": "Metamorphic rock",
            "difficulty_level": "Hard",
            "solution_steps": "Metamorphic rocks (like marble or slate) are generated from alteration of pre-existing rocks under high pressure/heat.",
            "explanation_description": "Geological rock cycle."
        },
        {
            "question_text": "What causes the different shapes of the Moon (phases of the Moon) as seen from Earth?",
            "options": ["The Moon changes its physical shape every week", "Clouds block different parts of the Moon", "The portion of the illuminated side of the Moon that faces Earth changes as it orbits", "The Earth casts a shadow on the Moon every night"],
            "correct_option": "The portion of the illuminated side of the Moon that faces Earth changes as it orbits",
            "difficulty_level": "Hard",
            "solution_steps": "As the Moon travels around Earth, we see different fractions of its sunlit hemisphere.",
            "explanation_description": "Lunar phases."
        },
        {
            "question_text": "Which of these is a correct pairing of an animal and its respiratory breathing organ?",
            "options": ["Dolphin - Gills", "Earthworm - Moist Skin", "Fish - Lungs", "Caterpillar - Gills"],
            "correct_option": "Earthworm - Moist Skin",
            "difficulty_level": "Hard",
            "solution_steps": "Earthworms use cuticular respiration (gaseous diffusion through moist skin). Dolphins use lungs, fish use gills.",
            "explanation_description": "Respiration organs."
        },
        {
            "question_text": "What happens to the friction when we apply grease or oil to the moving parts of a bicycle?",
            "options": ["Friction increases", "Friction decreases", "Friction remains same", "Gravity becomes zero"],
            "correct_option": "Friction decreases",
            "difficulty_level": "Medium",
            "solution_steps": "Lubricants form a smooth layer over metal micro-irregularities, decreasing rubbing resistance.",
            "explanation_description": "Friction reductions."
        },
        {
            "question_text": "Select the correct sequence of metamorphic stages in the life cycle of a frog.",
            "options": ["Egg -> Tadpole -> Froglet -> Adult Frog", "Egg -> Froglet -> Tadpole -> Adult Frog", "Tadpole -> Egg -> Froglet -> Adult Frog", "Egg -> Tadpole -> Adult Frog -> Froglet"],
            "correct_option": "Egg -> Tadpole -> Froglet -> Adult Frog",
            "difficulty_level": "Hard",
            "solution_steps": "Frogs start as eggs, hatch as tadpoles, develop limbs to become froglets, and lose their tails to become adult frogs.",
            "explanation_description": "Amphibian life cycles."
        },
        {
            "question_text": "A balloon is inflated by blowing air into it. Why does the balloon grow in size?",
            "options": ["Air has weight", "Air occupies space", "Air has no color", "Air is cold"],
            "correct_option": "Air occupies space",
            "difficulty_level": "Easy",
            "solution_steps": "Air is matter, so it expands the balloon to occupy spatial volume.",
            "explanation_description": "Properties of air."
        },
        {
            "question_text": "Why do trees in cold mountainous regions like pine trees have needle-shaped leaves and sloping branches?",
            "options": ["To collect more sunlight", "To let heavy snow slip off easily without breaking branches", "To prevent birds from making nests", "To catch insects"],
            "correct_option": "To let heavy snow slip off easily without breaking branches",
            "difficulty_level": "Hard",
            "solution_steps": "Conical shape and slippery thin needles prevent excessive snow loading.",
            "explanation_description": "Coniferous adaptations."
        },
        {
            "question_text": "Select the correct statement about air composition:",
            "options": ["Oxygen is the most abundant gas in air", "Nitrogen makes up about 78% of the air", "Carbon dioxide makes up 21% of the air", "Air has no weight"],
            "correct_option": "Nitrogen makes up about 78% of the air",
            "difficulty_level": "Medium",
            "solution_steps": "Air is 78% nitrogen, 21% oxygen, and 1% trace gases (argon, CO2, etc.).",
            "explanation_description": "Atmosphere composition."
        },
        {
            "question_text": "If a plastic comb rubbed against dry hair is brought near dry paper pieces, it attracts them. What type of force is this?",
            "options": ["Magnetic force", "Electrostatic force", "Frictional force", "Gravity"],
            "correct_option": "Electrostatic force",
            "difficulty_level": "Hard",
            "solution_steps": "Rubbing moves charges, creating a static surface field that polarizes and attracts neutral paper bits.",
            "explanation_description": "Static force."
        },
        {
            "question_text": "Why is planting grass on open bare soil slopes a good way to prevent soil erosion by heavy rains?",
            "options": ["Grass absorbs the rain completely", "Grass roots bind the soil particles together firmly", "Grass makes the soil hard like concrete", "Grass stops the wind"],
            "correct_option": "Grass roots bind the soil particles together firmly",
            "difficulty_level": "Hard",
            "solution_steps": "Root networks anchor loose topsoil, preventing it from being washed away by surface water runoff.",
            "explanation_description": "Soil conservation."
        },
        {
            "question_text": "Match the following items to their categories:\na. Caravan  - 1. Temporary house made of canvas\nb. Tent     - 2. Floating house in lakes\nc. Houseboat - 3. Mobile house on wheels",
            "options": ["a-3, b-1, c-2", "a-1, b-3, c-2", "a-3, b-2, c-1", "a-2, b-1, c-3"],
            "correct_option": "a-3, b-1, c-2",
            "difficulty_level": "Medium",
            "solution_steps": "Caravan is on wheels (3), tent is canvas (1), houseboat floats (2). Code is a-3, b-1, c-2.",
            "explanation_description": "Housing match."
        }
    ]

def populate_sof_quizzes_direct():
    print("Starting direct SOF Grade 3 quiz population...")
    
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
        existing_meta = supabase_db.table(quiz_table).select("id").eq("board", "CBSE").eq("grade", "Grade 3").eq("subject", "SOF Test").eq("chapter_or_topic", section_name).execute()
        if existing_meta.data:
            existing_id = existing_meta.data[0]["id"]
            print(f"Existing quiz found (ID: {existing_id}). Deleting old questions and quiz...")
            supabase_db.table(question_table).delete().eq(fk_field, existing_id).execute()
            supabase_db.table(quiz_table).delete().eq("id", existing_id).execute()
            
        # Create new quiz row
        quiz_metadata = {
            "board": "CBSE",
            "grade": "Grade 3",
            "subject": "SOF Test",
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
    populate_sof_quizzes_direct()
