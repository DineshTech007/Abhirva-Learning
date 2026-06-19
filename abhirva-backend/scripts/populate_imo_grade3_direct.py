import os
import sys

# Ensure the backend directory is in the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.supabase_client import supabase_db

def get_logical_reasoning():
    return [
        {
            "question_text": "Identify the pattern and find the next figure in the sequence: Circle, Triangle, Square, Circle, Triangle, ...",
            "options": ["Square", "Circle", "Pentagon", "Hexagon"],
            "correct_option": "Square",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern repeats every 3 figures: Circle -> Triangle -> Square. After Triangle, the next figure must be Square.",
            "explanation_description": "Standard repeating pattern sequence."
        },
        {
            "question_text": "If CAT is coded as DBU, how will DOG be coded in the same language?",
            "options": ["EPH", "ENF", "EOF", "CNE"],
            "correct_option": "EPH",
            "difficulty_level": "Easy",
            "solution_steps": "Each letter is replaced by its next alphabet: C -> D, A -> B, T -> U. Applying the same rule to DOG: D -> E, O -> P, G -> H. So DOG becomes EPH.",
            "explanation_description": "Coding/decoding with offset of +1."
        },
        {
            "question_text": "Rohan is 4th from the top and 12th from the bottom in a line of students. How many students are there in the line?",
            "options": ["16", "15", "17", "14"],
            "correct_option": "15",
            "difficulty_level": "Medium",
            "solution_steps": "Total students = Position from top + Position from bottom - 1. So, 4 + 12 - 1 = 15.",
            "explanation_description": "Line ranking calculation."
        },
        {
            "question_text": "If today is Wednesday, what day of the week will it be 3 days after tomorrow?",
            "options": ["Saturday", "Sunday", "Friday", "Monday"],
            "correct_option": "Sunday",
            "difficulty_level": "Medium",
            "solution_steps": "Today is Wednesday. Tomorrow will be Thursday. 3 days after Thursday is: Friday (1), Saturday (2), Sunday (3).",
            "explanation_description": "Calendar day offset calculation."
        },
        {
            "question_text": "Which number replaces the question mark (?) in the number pattern: 5, 10, 15, 20, ?, 30?",
            "options": ["22", "24", "25", "28"],
            "correct_option": "25",
            "difficulty_level": "Easy",
            "solution_steps": "The pattern is adding 5 to each term: 5+5=10, 10+5=15, 15+5=20, 20+5=25.",
            "explanation_description": "Basic arithmetic number sequence."
        },
        {
            "question_text": "How many squares are there in a 2x2 grid?",
            "options": ["4", "5", "6", "3"],
            "correct_option": "5",
            "difficulty_level": "Medium",
            "solution_steps": "A 2x2 grid has four 1x1 small squares, and one large 2x2 square. Total = 4 + 1 = 5 squares.",
            "explanation_description": "Geometric shape counting."
        },
        {
            "question_text": "In a certain code, 'BLUE' is written as 'EUBL'. How is 'PINK' written in that code?",
            "options": ["KNIP", "KPIN", "KPIK", "NKIP"],
            "correct_option": "KPIN",
            "difficulty_level": "Medium",
            "solution_steps": "The code rearranges BLUE to EUBL: the last letter (E) comes first, followed by the first letter (B), then the second (L), then third (U). Re-arranging PINK similarly gives KPIN.",
            "explanation_description": "Character position rearrangement cipher."
        },
        {
            "question_text": "Find the odd one out among the following options:",
            "options": ["Car", "Bicycle", "Boat", "Bus"],
            "correct_option": "Boat",
            "difficulty_level": "Easy",
            "solution_steps": "Car, Bicycle, and Bus are land transportation, whereas Boat is water transportation.",
            "explanation_description": "Classification based on media of transport."
        },
        {
            "question_text": "Which figure is the correct mirror image of the capital letter 'E' when the mirror is placed to its right?",
            "options": ["E", "F", "3 (reversed)", "∃ (flipped E)"],
            "correct_option": "∃ (flipped E)",
            "difficulty_level": "Easy",
            "solution_steps": "Mirror image of 'E' flips horizontally, facing left instead of right.",
            "explanation_description": "Horizontal mirror reflection test."
        },
        {
            "question_text": "What is the next term in the alphabet pattern: Z, X, V, T, R, ?",
            "options": ["P", "Q", "S", "O"],
            "correct_option": "P",
            "difficulty_level": "Medium",
            "solution_steps": "The pattern skips one letter backwards: Z(-2)->X(-2)->V(-2)->T(-2)->R(-2)->P.",
            "explanation_description": "Decrementing alphabet sequence."
        },
        {
            "question_text": "A clock shows the time as 3:15. If the minute hand points to the East, in which direction does the hour hand point?",
            "options": ["North", "South", "East", "West"],
            "correct_option": "East",
            "difficulty_level": "Medium",
            "solution_steps": "At 3:15, both hands point near 3, which is the East direction.",
            "explanation_description": "Clock hand alignment mapping."
        },
        {
            "question_text": "There are 4 boys: Sam, Tom, Jerry, and Spike. Sam is taller than Tom but shorter than Jerry. Jerry is shorter than Spike. Who is the tallest?",
            "options": ["Sam", "Tom", "Jerry", "Spike"],
            "correct_option": "Spike",
            "difficulty_level": "Medium",
            "solution_steps": "Tom < Sam < Jerry < Spike. Therefore, Spike is the tallest.",
            "explanation_description": "Relative height ordering."
        },
        {
            "question_text": "How many corners (vertices) does a standard cuboid have?",
            "options": ["6", "8", "12", "4"],
            "correct_option": "8",
            "difficulty_level": "Easy",
            "solution_steps": "A cuboid has 6 faces, 12 edges, and 8 corners (vertices).",
            "explanation_description": "3D shape geometry properties."
        },
        {
            "question_text": "If triangle represents 3, square represents 4, and circle represents 5, what is the value of: Triangle + Square - Circle?",
            "options": ["2", "12", "7", "5"],
            "correct_option": "2",
            "difficulty_level": "Easy",
            "solution_steps": "Substitute the values: 3 + 4 - 5 = 7 - 5 = 2.",
            "explanation_description": "Symbolic substitution arithmetic."
        },
        {
            "question_text": "Find the missing number in the grid:\n[ 2 ] [ 4 ] [ 6 ]\n[ 3 ] [ 6 ] [ 9 ]\n[ 4 ] [ 8 ] [ ? ]",
            "options": ["10", "12", "14", "16"],
            "correct_option": "12",
            "difficulty_level": "Medium",
            "solution_steps": "Row 1: 2 * 1 = 2, 2 * 2 = 4, 2 * 3 = 6.\nRow 2: 3 * 1 = 3, 3 * 2 = 6, 3 * 3 = 9.\nRow 3: 4 * 1 = 4, 4 * 2 = 8, 4 * 3 = 12.",
            "explanation_description": "Grid multiplication pattern."
        },
        {
            "question_text": "Which of the following figures can be folded to make a perfect cube?",
            "options": ["T-shape of 6 squares", "Line of 5 squares", "L-shape of 4 squares", "Square grid of 2x3"],
            "correct_option": "T-shape of 6 squares",
            "difficulty_level": "Hard",
            "solution_steps": "A T-shape consisting of 6 squares is a standard net diagram that can fold into a cube.",
            "explanation_description": "3D nets and spatial reasoning."
        },
        {
            "question_text": "Complete the analogy: Day is to Sun as Night is to ____________.",
            "options": ["Star", "Moon", "Darkness", "Sky"],
            "correct_option": "Moon",
            "difficulty_level": "Easy",
            "solution_steps": "The Sun shines in the sky during the Day, and the Moon is the primary body shining in the sky at Night.",
            "explanation_description": "Analogical relationship reasoning."
        },
        {
            "question_text": "A bird flies 2 meters North, then turns right and flies 3 meters East, then turns right and flies 2 meters South. How far is the bird from its starting point?",
            "options": ["2 meters", "3 meters", "5 meters", "0 meters"],
            "correct_option": "3 meters",
            "difficulty_level": "Medium",
            "solution_steps": "The bird's path forms a rectangle: 2m North, 3m East, 2m South. The bird is now exactly 3m East of its starting point.",
            "explanation_description": "Directional distance mapping."
        },
        {
            "question_text": "If all cats are animals, and some animals are dogs, which of the following is definitely true?",
            "options": ["All dogs are cats", "Some dogs are cats", "Cats are animals", "Dogs are cats"],
            "correct_option": "Cats are animals",
            "difficulty_level": "Easy",
            "solution_steps": "The statement directly states that 'all cats are animals', so 'Cats are animals' is definitely true.",
            "explanation_description": "Basic logical deduction."
        },
        {
            "question_text": "If a pair of scissors is called 'comb', comb is called 'brush', and brush is called 'mirror', what do we use to tidy our hair?",
            "options": ["comb", "brush", "mirror", "scissors"],
            "correct_option": "brush",
            "difficulty_level": "Medium",
            "solution_steps": "Normally we use a comb to tidy our hair. But in this code, 'comb' is called 'brush'. So we use 'brush'.",
            "explanation_description": "Substitution cipher puzzle."
        },
        {
            "question_text": "How many triangles are there in a square with both diagonals drawn?",
            "options": ["4", "6", "8", "10"],
            "correct_option": "8",
            "difficulty_level": "Hard",
            "solution_steps": "A square with 2 diagonals has: 4 small triangles (1 quadrant each), and 4 large triangles (formed by combining 2 quadrants along diagonals). Total = 8 triangles.",
            "explanation_description": "Complex shape counting."
        },
        {
            "question_text": "If you write all numbers from 1 to 20, how many times do you write the digit '2'?",
            "options": ["2", "3", "4", "1"],
            "correct_option": "3",
            "difficulty_level": "Medium",
            "solution_steps": "The numbers containing the digit '2' from 1 to 20 are: 2, 12, and 20. The digit '2' appears exactly 3 times.",
            "explanation_description": "Digit counting puzzle."
        },
        {
            "question_text": "Anish has 5 crayons. Biplab has twice as many crayons as Anish. Charlie has 3 fewer crayons than Biplab. How many crayons does Charlie have?",
            "options": ["10", "7", "8", "5"],
            "correct_option": "7",
            "difficulty_level": "Medium",
            "solution_steps": "Anish = 5. Biplab = 5 * 2 = 10. Charlie = 10 - 3 = 7.",
            "explanation_description": "Sequential comparison reasoning."
        },
        {
            "question_text": "Identify the next number in the pattern: 2, 4, 8, 16, ?",
            "options": ["20", "24", "32", "30"],
            "correct_option": "32",
            "difficulty_level": "Easy",
            "solution_steps": "Each term is multiplied by 2: 2*2=4, 4*2=8, 8*2=16, 16*2=32.",
            "explanation_description": "Geometric doubling sequence."
        },
        {
            "question_text": "Which of these words cannot be formed using the letters of the word 'OLYMPIAD'?",
            "options": ["PLAY", "LAMP", "DAMP", "MAIL"],
            "correct_option": "MAIL",
            "difficulty_level": "Easy",
            "solution_steps": "'MAIL' contains the letter 'R' or 'I'... wait, OLYMPIAD has I, M, A, L (M-A-I-L are all present). 'PLAY' has P, L, A, Y. 'LAMP' has L, A, M, P. 'DAMP' has D, A, M, P. Wait! Let's choose another word. What about 'PAIN'? OLYMPIAD has no 'N'. So 'PAIN' cannot be formed.",
            "options": ["PLAY", "LAMP", "PAIN", "DAMP"],
            "correct_option": "PAIN",
            "difficulty_level": "Easy",
            "solution_steps": "The word 'PAIN' has the letter 'N', which is not present in the word 'OLYMPIAD'.",
            "explanation_description": "Letter spelling check."
        }
    ]

def get_mathematical_reasoning():
    return [
        {
            "question_text": "What is the place value of the digit 7 in the number 4785?",
            "options": ["7", "70", "700", "7000"],
            "correct_option": "700",
            "difficulty_level": "Easy",
            "solution_steps": "In 4785, 5 is at ones place, 8 is at tens place, 7 is at hundreds place, and 4 is at thousands place. So, place value of 7 is 700.",
            "explanation_description": "Standard place value identification."
        },
        {
            "question_text": "Subtract 2845 from 6000. What is the result?",
            "options": ["3155", "3255", "4155", "3165"],
            "correct_option": "3155",
            "difficulty_level": "Medium",
            "solution_steps": "6000 - 2845 = 3155.",
            "explanation_description": "Four-digit subtraction with borrowing."
        },
        {
            "question_text": "Which of the following is equivalent to: 8000 + 40 + 7?",
            "options": ["8407", "8047", "8470", "80047"],
            "correct_option": "8047",
            "difficulty_level": "Easy",
            "solution_steps": "8000 + 40 + 7 = 8047 (8 thousands, 0 hundreds, 4 tens, 7 ones).",
            "explanation_description": "Expanded form calculation."
        },
        {
            "question_text": "If one pencil costs $4, what is the cost of 15 such pencils?",
            "options": ["$45", "$60", "$55", "$70"],
            "correct_option": "$60",
            "difficulty_level": "Easy",
            "solution_steps": "Cost of 15 pencils = 15 * $4 = $60.",
            "explanation_description": "Single-digit multiplication."
        },
        {
            "question_text": "Divide 156 by 6. What is the quotient?",
            "options": ["24", "26", "28", "25"],
            "correct_option": "26",
            "difficulty_level": "Medium",
            "solution_steps": "156 / 6 = 26. Since 6 * 20 = 120, and 6 * 6 = 36. 120 + 36 = 156.",
            "explanation_description": "Short division calculation."
        },
        {
            "question_text": "What fraction of the letters in the word 'MATHEMATICS' are vowels?",
            "options": ["4/11", "3/11", "5/11", "4/10"],
            "correct_option": "4/11",
            "difficulty_level": "Medium",
            "solution_steps": "Total letters in MATHEMATICS = 11. Vowels are A, E, A, I (4 vowels). So, fraction is 4/11.",
            "explanation_description": "Fraction of a set."
        },
        {
            "question_text": "How many millimeters are there in 5 centimeters?",
            "options": ["50 mm", "500 mm", "5 mm", "5000 mm"],
            "correct_option": "50 mm",
            "difficulty_level": "Easy",
            "solution_steps": "1 cm = 10 mm. Therefore, 5 cm = 5 * 10 = 50 mm.",
            "explanation_description": "Length unit conversion."
        },
        {
            "question_text": "A box contains 3 kg 450 g of sugar. If 1 kg 200 g of sugar is used, how much sugar is left in the box?",
            "options": ["2 kg 250 g", "2 kg 150 g", "1 kg 250 g", "2 kg 350 g"],
            "correct_option": "2 kg 250 g",
            "difficulty_level": "Medium",
            "solution_steps": "3 kg 450 g - 1 kg 200 g = 2 kg 250 g.",
            "explanation_description": "Weight subtraction without borrowing."
        },
        {
            "question_text": "Which of these clocks displays 15 minutes past 8?",
            "options": ["8:15", "8:45", "9:15", "7:45"],
            "correct_option": "8:15",
            "difficulty_level": "Easy",
            "solution_steps": "15 minutes past 8 is written numerically as 8:15.",
            "explanation_description": "Time reading comprehension."
        },
        {
            "question_text": "What is the perimeter of a rectangle with a length of 8 cm and a width of 5 cm?",
            "options": ["13 cm", "26 cm", "40 cm", "20 cm"],
            "correct_option": "26 cm",
            "difficulty_level": "Medium",
            "solution_steps": "Perimeter of rectangle = 2 * (length + width) = 2 * (8 + 5) = 2 * 13 = 26 cm.",
            "explanation_description": "Perimeter geometry calculation."
        },
        {
            "question_text": "Convert 3 liters into milliliters.",
            "options": ["30 mL", "300 mL", "3000 mL", "30000 mL"],
            "correct_option": "3000 mL",
            "difficulty_level": "Easy",
            "solution_steps": "1 liter = 1000 mL. So, 3 liters = 3 * 1000 = 3000 mL.",
            "explanation_description": "Capacity unit conversion."
        },
        {
            "question_text": "What number must be added to 345 to get 800?",
            "options": ["455", "555", "355", "465"],
            "correct_option": "455",
            "difficulty_level": "Medium",
            "solution_steps": "Required number = 800 - 345 = 455.",
            "explanation_description": "Inverse operation calculations."
        },
        {
            "question_text": "Which of the following numbers is an even number?",
            "options": ["4567", "5679", "3450", "1235"],
            "correct_option": "3450",
            "difficulty_level": "Easy",
            "solution_steps": "Even numbers end with 0, 2, 4, 6, or 8. Out of the options, only 3450 ends with 0.",
            "explanation_description": "Even and odd number identification."
        },
        {
            "question_text": "How many vertices (corners) does a triangle have?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "3",
            "difficulty_level": "Easy",
            "solution_steps": "A triangle has 3 sides and 3 vertices.",
            "explanation_description": "Basic geometric properties."
        },
        {
            "question_text": "Which sign makes the statement true: 345 + 125 ____ 600 - 150?",
            "options": [">", "<", "=", "+"],
            "correct_option": ">",
            "difficulty_level": "Medium",
            "solution_steps": "Left Hand Side = 345 + 125 = 470. Right Hand Side = 600 - 150 = 450. Since 470 is greater than 450, the symbol is >.",
            "explanation_description": "Arithmetic comparison."
        },
        {
            "question_text": "What is the sum of the smallest 3-digit number and the largest 2-digit number?",
            "options": ["199", "100", "99", "109"],
            "correct_option": "199",
            "difficulty_level": "Medium",
            "solution_steps": "Smallest 3-digit number = 100. Largest 2-digit number = 99. Sum = 100 + 99 = 199.",
            "explanation_description": "Digit value reasoning."
        },
        {
            "question_text": "If 4 triangles represent 20 apples, how many apples does one triangle represent?",
            "options": ["4", "5", "10", "6"],
            "correct_option": "5",
            "difficulty_level": "Easy",
            "solution_steps": "If 4 triangles = 20 apples, then 1 triangle = 20 / 4 = 5 apples.",
            "explanation_description": "Pictograph scaling calculation."
        },
        {
            "question_text": "What is the fraction of the unshaded portion in a circle divided into 8 equal parts with 3 parts shaded?",
            "options": ["3/8", "5/8", "1/2", "8/5"],
            "correct_option": "5/8",
            "difficulty_level": "Medium",
            "solution_steps": "Total parts = 8. Shaded parts = 3. Unshaded parts = 8 - 3 = 5. Unshaded fraction = 5/8.",
            "explanation_description": "Visual fractions interpretation."
        },
        {
            "question_text": "Which of the following is another way to write 4 x 6?",
            "options": ["4 + 4 + 4 + 4", "6 + 6 + 6 + 6", "4 + 6", "6 + 6 + 6 + 6 + 6 + 6"],
            "correct_option": "6 + 6 + 6 + 6",
            "difficulty_level": "Easy",
            "solution_steps": "4 x 6 means adding 6 four times, which is 6 + 6 + 6 + 6.",
            "explanation_description": "Repeated addition equivalence."
        },
        {
            "question_text": "Identify the shape that has no straight sides and no corners.",
            "options": ["Triangle", "Square", "Circle", "Pentagon"],
            "correct_option": "Circle",
            "difficulty_level": "Easy",
            "solution_steps": "A circle is bounded by a single curved line and has no vertices (corners) or straight edges.",
            "explanation_description": "Basic geometry properties."
        },
        {
            "question_text": "How many days are there in a leap year?",
            "options": ["365", "366", "364", "360"],
            "correct_option": "366",
            "difficulty_level": "Easy",
            "solution_steps": "A normal year has 365 days, whereas a leap year has 366 days (with 29 days in February).",
            "explanation_description": "Calendar logic."
        },
        {
            "question_text": "If you multiply any number by zero, what is the answer?",
            "options": ["The number itself", "Zero", "One", "Double the number"],
            "correct_option": "Zero",
            "difficulty_level": "Easy",
            "solution_steps": "Any number multiplied by 0 always results in 0.",
            "explanation_description": "Zero property of multiplication."
        },
        {
            "question_text": "What is the value of 350 + 250 - 100?",
            "options": ["500", "600", "400", "550"],
            "correct_option": "500",
            "difficulty_level": "Easy",
            "solution_steps": "Perform operations from left to right: 350 + 250 = 600. Then 600 - 100 = 500.",
            "explanation_description": "Addition and subtraction order."
        },
        {
            "question_text": "How many faces does a sphere have?",
            "options": ["1", "2", "0", "3"],
            "correct_option": "1",
            "difficulty_level": "Medium",
            "solution_steps": "A sphere has exactly 1 curved face and no flat faces or edges.",
            "explanation_description": "3D shape geometry properties."
        },
        {
            "question_text": "Add: 247 + 583. What is the sum?",
            "options": ["830", "820", "730", "840"],
            "correct_option": "830",
            "difficulty_level": "Easy",
            "solution_steps": "247 + 583: 7+3=10 (carry 1), 4+8+1=13 (carry 1), 2+5+1=8. Sum is 830.",
            "explanation_description": "Addition of 3-digit numbers with carrying."
        }
    ]

def get_everyday_mathematics():
    return [
        {
            "question_text": "A school bus has 45 seats. If 32 children are sitting in the bus, how many seats are empty?",
            "options": ["13", "12", "15", "10"],
            "correct_option": "13",
            "difficulty_level": "Easy",
            "solution_steps": "Empty seats = Total seats - Children sitting = 45 - 32 = 13.",
            "explanation_description": "Everyday subtraction problem."
        },
        {
            "question_text": "Ram bought a notebook for $35, a pen for $12, and an eraser for $5. He gave a $100 note to the shopkeeper. How much change will he get back?",
            "options": ["$48", "$52", "$58", "$62"],
            "correct_option": "$48",
            "difficulty_level": "Medium",
            "solution_steps": "Total spend = $35 + $12 + $5 = $52. Change back = $100 - $52 = $48.",
            "explanation_description": "Multi-step money word problem."
        },
        {
            "question_text": "A box of chocolates contains 24 chocolates. If 4 children share them equally, how many chocolates does each child get?",
            "options": ["6", "8", "4", "5"],
            "correct_option": "6",
            "difficulty_level": "Easy",
            "solution_steps": "Chocolates per child = Total chocolates / Number of children = 24 / 4 = 6.",
            "explanation_description": "Equal sharing division problem."
        },
        {
            "question_text": "Sita reads 8 pages of a book every day. How many pages will she read in 2 weeks?",
            "options": ["16", "56", "112", "80"],
            "correct_option": "112",
            "difficulty_level": "Medium",
            "solution_steps": "2 weeks = 14 days. Total pages read = 8 pages/day * 14 days = 112 pages.",
            "explanation_description": "Time conversion and multiplication word problem."
        },
        {
            "question_text": "A tank had 500 liters of water. In the morning, 120 liters were used, and in the evening, 180 liters were used. How much water is left in the tank?",
            "options": ["200 liters", "300 liters", "150 liters", "250 liters"],
            "correct_option": "200 liters",
            "difficulty_level": "Medium",
            "solution_steps": "Total water used = 120 + 180 = 300 liters. Water left = 500 - 300 = 200 liters.",
            "explanation_description": "Water capacity usage word problem."
        },
        {
            "question_text": "Anil goes to bed at 9:30 p.m. and wakes up at 6:30 a.m. the next morning. For how many hours does he sleep?",
            "options": ["8 hours", "9 hours", "10 hours", "7 hours"],
            "correct_option": "9 hours",
            "difficulty_level": "Medium",
            "solution_steps": "From 9:30 p.m. to 12:00 midnight is 2 hours 30 mins. From midnight to 6:30 a.m. is 6 hours 30 mins. Total sleep = 2.5 + 6.5 = 9 hours.",
            "explanation_description": "Time elapsed calculation."
        },
        {
            "question_text": "Each cookie packet has 6 cookies. If Mother buys 7 packets, how many cookies does she have in total?",
            "options": ["42", "36", "48", "40"],
            "correct_option": "42",
            "difficulty_level": "Easy",
            "solution_steps": "Total cookies = 7 packets * 6 cookies/packet = 42 cookies.",
            "explanation_description": "Everyday multiplication problem."
        },
        {
            "question_text": "A toy train costs $145. A toy plane costs $80 more than the toy train. What is the cost of the toy plane?",
            "options": ["$225", "$205", "$165", "$180"],
            "correct_option": "$225",
            "difficulty_level": "Easy",
            "solution_steps": "Cost of toy plane = Cost of train + $80 = $145 + $80 = $225.",
            "explanation_description": "Comparison addition word problem."
        },
        {
            "question_text": "In a library, there are 345 English books, 218 Science books, and 190 Math books. How many books are there in total?",
            "options": ["753", "743", "653", "763"],
            "correct_option": "753",
            "difficulty_level": "Medium",
            "solution_steps": "Total books = 345 + 218 + 190 = 753.",
            "explanation_description": "Three-number addition word problem."
        },
        {
            "question_text": "A garden has 9 rows of rose plants. If there are 12 plants in each row, how many rose plants are there in the garden?",
            "options": ["108", "98", "118", "90"],
            "correct_option": "108",
            "difficulty_level": "Easy",
            "solution_steps": "Total plants = 9 rows * 12 plants/row = 108 rose plants.",
            "explanation_description": "Grid arrangement multiplication."
        },
        {
            "question_text": "Meera has 4 meters of ribbon. She cuts it into 8 equal pieces. What is the length of each piece in centimeters?",
            "options": ["50 cm", "40 cm", "25 cm", "30 cm"],
            "correct_option": "50 cm",
            "difficulty_level": "Medium",
            "solution_steps": "Total length = 4 meters = 400 cm. Length of each piece = 400 cm / 8 = 50 cm.",
            "explanation_description": "Measurement conversion and division."
        },
        {
            "question_text": "In a cricket match, Rohit scored 87 runs. He needs how many more runs to complete a century (100 runs)?",
            "options": ["13", "23", "17", "15"],
            "correct_option": "13",
            "difficulty_level": "Easy",
            "solution_steps": "Runs needed = 100 - 87 = 13 runs.",
            "explanation_description": "Sports-themed subtraction word problem."
        },
        {
            "question_text": "A fruit vendor had 120 apples. He sold 45 apples on Monday and 35 apples on Tuesday. How many apples are left with him?",
            "options": ["40", "50", "60", "30"],
            "correct_option": "40",
            "difficulty_level": "Medium",
            "solution_steps": "Total apples sold = 45 + 35 = 80 apples. Apples left = 120 - 80 = 40 apples.",
            "explanation_description": "Two-step subtraction word problem."
        },
        {
            "question_text": "A packet of potato chips costs $15. If Rahul buy 5 packets and gives a $100 bill, how much change should he receive?",
            "options": ["$25", "$35", "$75", "$15"],
            "correct_option": "$25",
            "difficulty_level": "Medium",
            "solution_steps": "Total cost = 5 * $15 = $75. Change = $100 - $75 = $25.",
            "explanation_description": "Everyday shopping math."
        },
        {
            "question_text": "A farmer harvested 56 kg of potatoes. He packed them equally into 7 bags. What is the weight of each bag?",
            "options": ["8 kg", "7 kg", "9 kg", "6 kg"],
            "correct_option": "8 kg",
            "difficulty_level": "Easy",
            "solution_steps": "Weight per bag = 56 kg / 7 bags = 8 kg.",
            "explanation_description": "Equal distribution weight division."
        },
        {
            "question_text": "A theater play started at 4:15 p.m. and ended at 5:45 p.m. How long did the play last?",
            "options": ["1 hour 30 minutes", "1 hour 15 minutes", "2 hours", "1 hour"],
            "correct_option": "1 hour 30 minutes",
            "difficulty_level": "Medium",
            "solution_steps": "From 4:15 to 5:15 is 1 hour. From 5:15 to 5:45 is 30 minutes. Total time is 1 hour 30 minutes.",
            "explanation_description": "Time duration word problem."
        },
        {
            "question_text": "A rope is 12 meters long. If a piece of 3 meters 50 cm is cut off, what is the length of the remaining rope?",
            "options": ["8 m 50 cm", "9 m 50 cm", "7 m 50 cm", "8 m"],
            "correct_option": "8 m 50 cm",
            "difficulty_level": "Medium",
            "solution_steps": "12 m = 1200 cm. Cut piece = 350 cm. Remaining = 1200 - 350 = 850 cm = 8 m 50 cm.",
            "explanation_description": "Length subtraction word problem."
        },
        {
            "question_text": "A bakery sold 150 vanilla cupcakes and 220 strawberry cupcakes. How many cupcakes did they sell in all?",
            "options": ["370", "360", "270", "380"],
            "correct_option": "370",
            "difficulty_level": "Easy",
            "solution_steps": "Total cupcakes sold = 150 + 220 = 370.",
            "explanation_description": "Simple addition word problem."
        },
        {
            "question_text": "There are 48 students in a classroom. If they are divided into 6 equal groups, how many students are in each group?",
            "options": ["8", "7", "9", "6"],
            "correct_option": "8",
            "difficulty_level": "Easy",
            "solution_steps": "Students per group = 48 / 6 = 8.",
            "explanation_description": "Grouping division word problem."
        },
        {
            "question_text": "A milk container holds 10 liters of milk. If 4 liters 250 mL of milk is sold, how much milk is left in the container?",
            "options": ["5 L 750 mL", "5 L 250 mL", "6 L 750 mL", "6 L"],
            "correct_option": "5 L 750 mL",
            "difficulty_level": "Medium",
            "solution_steps": "10 L = 10000 mL. Sold = 4250 mL. Left = 10000 - 4250 = 5750 mL = 5 L 750 mL.",
            "explanation_description": "Capacity subtraction word problem."
        },
        {
            "question_text": "Kunal has 15 red marbles and 25 blue marbles. He wants to pack them into packets containing 5 marbles each. How many packets does he need?",
            "options": ["8", "7", "6", "9"],
            "correct_option": "8",
            "difficulty_level": "Medium",
            "solution_steps": "Total marbles = 15 + 25 = 40. Packets needed = 40 / 5 = 8.",
            "explanation_description": "Two-step addition and division word problem."
        },
        {
            "question_text": "A school has 4 sections of Grade 3. If there are 30 students in each section, how many Grade 3 students are there in the school?",
            "options": ["120", "100", "90", "150"],
            "correct_option": "120",
            "difficulty_level": "Easy",
            "solution_steps": "Total students = 4 * 30 = 120.",
            "explanation_description": "Grade-level multiplication word problem."
        },
        {
            "question_text": "A fruit box contains 15 apples. If 3 apples are rotten, what fraction of the apples in the box are good?",
            "options": ["4/5", "1/5", "3/5", "2/5"],
            "correct_option": "4/5",
            "difficulty_level": "Medium",
            "solution_steps": "Good apples = 15 - 3 = 12. Fraction of good apples = 12/15 = 4/5.",
            "explanation_description": "Fraction word problem with simplification."
        },
        {
            "question_text": "A toy car travels 15 meters in 1 minute. How far will it travel in 5 minutes if it continues at the same speed?",
            "options": ["75 meters", "60 meters", "50 meters", "80 meters"],
            "correct_option": "75 meters",
            "difficulty_level": "Easy",
            "solution_steps": "Distance = Speed * Time = 15 meters/minute * 5 minutes = 75 meters.",
            "explanation_description": "Distance calculation word problem."
        },
        {
            "question_text": "A candle is 25 cm long. After burning for an hour, its length is 18 cm. How much of the candle burned away?",
            "options": ["7 cm", "8 cm", "6 cm", "9 cm"],
            "correct_option": "7 cm",
            "difficulty_level": "Easy",
            "solution_steps": "Burned length = Initial length - Final length = 25 cm - 18 cm = 7 cm.",
            "explanation_description": "Simple subtraction word problem."
        }
    ]

def get_achievers_section():
    return [
        {
            "question_text": "If ⏶ + ⏶ + ◼ = 18 and ◼ + ◼ + ⏶ = 15, what is the value of ⏶ + ◼?",
            "options": ["11", "9", "12", "10"],
            "correct_option": "11",
            "difficulty_level": "Hard",
            "solution_steps": "Let triangle = T, square = S. 2T + S = 18 and 2S + T = 15. Adding the two equations: 3T + 3S = 33. Dividing by 3: T + S = 11.",
            "explanation_description": "System of symbolic equations."
        },
        {
            "question_text": "Find the values of P and Q respectively:\n  3  P  4\n+ Q  5  8\n---------\n  8  3  2",
            "options": ["P = 7, Q = 4", "P = 8, Q = 4", "P = 7, Q = 5", "P = 6, Q = 4"],
            "correct_option": "P = 7, Q = 4",
            "difficulty_level": "Hard",
            "solution_steps": "Looking at ones column: 4 + 8 = 12 (write 2, carry 1). Tens column: P + 5 + 1 (carry) = 13 (write 3, carry 1) => P + 6 = 13 => P = 7. Hundreds column: 3 + Q + 1 (carry) = 8 => 4 + Q = 8 => Q = 4. So P = 7 and Q = 4.",
            "explanation_description": "Cryptarithmetic column addition puzzle."
        },
        {
            "question_text": "A container is 1/4 full of water. When 6 liters of water are added, the container becomes 1/2 full. What is the total capacity of the container?",
            "options": ["24 liters", "12 liters", "18 liters", "30 liters"],
            "correct_option": "24 liters",
            "difficulty_level": "Hard",
            "solution_steps": "Let capacity be C. 1/2 * C - 1/4 * C = 6 liters => 1/4 * C = 6 => C = 24 liters.",
            "explanation_description": "Fractional container capacity word problem."
        },
        {
            "question_text": "A clock strikes once at 1 o'clock, twice at 2 o'clock, thrice at 3 o'clock, and so on. How many times will it strike in total from 1 o'clock to 6 o'clock?",
            "options": ["21 times", "18 times", "15 times", "24 times"],
            "correct_option": "21 times",
            "difficulty_level": "Hard",
            "solution_steps": "Total strikes = 1 + 2 + 3 + 4 + 5 + 6 = 21 strikes.",
            "explanation_description": "Arithmetic progression sum."
        },
        {
            "question_text": "Five friends stood in a line. Amit is second in line. Chetan is immediately behind Amit. Dinesh is in front of Amit. If Esha is behind Chetan and Bimal is behind Esha, who is last in the line?",
            "options": ["Bimal", "Esha", "Chetan", "Amit"],
            "correct_option": "Bimal",
            "difficulty_level": "Hard",
            "solution_steps": "Line order from front to back:\n1st: Dinesh (in front of Amit)\n2nd: Amit (second in line)\n3rd: Chetan (immediately behind Amit)\n4th: Esha (behind Chetan)\n5th: Bimal (behind Esha). So Bimal is last.",
            "explanation_description": "Logical arrangement grid puzzle."
        },
        {
            "question_text": "A rectangular playground has a perimeter of 40 meters. If its length is 12 meters, what is its width?",
            "options": ["8 meters", "14 meters", "16 meters", "6 meters"],
            "correct_option": "8 meters",
            "difficulty_level": "Hard",
            "solution_steps": "Perimeter = 2 * (length + width) = 40. Length + width = 20. Width = 20 - 12 = 8 meters.",
            "explanation_description": "Perimeter inverse problem."
        },
        {
            "question_text": "A frog is at the bottom of a 10-meter deep well. Each day it climbs up 3 meters, but slips back 2 meters during the night. How many days will it take for the frog to reach the top of the well?",
            "options": ["8 days", "10 days", "7 days", "9 days"],
            "correct_option": "8 days",
            "difficulty_level": "Hard",
            "solution_steps": "Each day the frog net climbs 3 - 2 = 1 meter. By the end of day 7, it is at 7 meters. On day 8, it climbs 3 meters and reaches 10 meters, climbing out of the well before it can slip.",
            "explanation_description": "Classic climbing riddle."
        },
        {
            "question_text": "If 3 apples cost as much as 4 bananas, and 2 bananas cost $1.50, how much do 6 apples cost?",
            "options": ["$6.00", "$8.00", "$9.00", "$4.50"],
            "correct_option": "$6.00",
            "difficulty_level": "Hard",
            "solution_steps": "2 bananas = $1.50 => 1 banana = $0.75. 4 bananas = 4 * 0.75 = $3.00. Since 3 apples = 4 bananas, 3 apples cost $3.00 => 1 apple = $1.00. So, 6 apples cost 6 * $1.00 = $6.00.",
            "explanation_description": "Multi-step conversion and equivalence."
        },
        {
            "question_text": "Which digit should go into the box to make the statement true?\n789 - [ ]45 = 444",
            "options": ["3", "4", "2", "5"],
            "correct_option": "3",
            "difficulty_level": "Hard",
            "solution_steps": "789 - X = 444 => X = 789 - 444 = 345. Thus, the missing hundreds digit in [ ]45 is 3.",
            "explanation_description": "Arithmetic missing digit deduction."
        },
        {
            "question_text": "In a box, half of the marbles are blue, one-quarter are red, and the remaining 8 marbles are green. How many total marbles are in the box?",
            "options": ["32", "16", "24", "40"],
            "correct_option": "32",
            "difficulty_level": "Hard",
            "solution_steps": "Blue fraction = 1/2. Red fraction = 1/4. Together Blue + Red = 3/4. Green fraction is 1 - 3/4 = 1/4. If 1/4 of total marbles = 8, then total marbles = 8 * 4 = 32.",
            "explanation_description": "Fractions word problem."
        },
        {
            "question_text": "Find the sum of all two-digit numbers that have the digit 5 at both the tens place and ones place.",
            "options": ["55", "110", "50", "105"],
            "correct_option": "55",
            "difficulty_level": "Medium",
            "solution_steps": "The only two-digit number with 5 at both tens and ones place is 55. The sum of this single number is 55.",
            "explanation_description": "Place value criteria check."
        },
        {
            "question_text": "If A x B = 24 and A - B = 2 (where A and B are positive numbers), what is the value of A + B?",
            "options": ["10", "14", "8", "12"],
            "correct_option": "10",
            "difficulty_level": "Hard",
            "solution_steps": "Pairs multiplying to 24: (24, 1), (12, 2), (8, 3), (6, 4). The pair with a difference of 2 is (6, 4). So A = 6, B = 4. A + B = 6 + 4 = 10.",
            "explanation_description": "Factor pair optimization puzzle."
        },
        {
            "question_text": "A train starts from Station A with 120 passengers. At Station B, 45 passengers get down and 30 passengers get in. At Station C, half of the passengers get down. How many passengers are left on the train?",
            "options": ["52", "53", "55", "50"],
            "correct_option": "52",
            "difficulty_level": "Hard",
            "solution_steps": "Start = 120. Station B = 120 - 45 + 30 = 105 passengers. Wait, let's re-verify: 120 - 45 = 75. 75 + 30 = 105. At Station C, half get down. Half of 105 is 52.5 (not a whole number). Let's change the numbers. Let's make it: At Station B, 45 passengers get down and 29 passengers get in. 120 - 45 + 29 = 104. At Station C, half get down, leaving 52 passengers.",
            "options": ["52", "55", "60", "48"],
            "correct_option": "52",
            "difficulty_level": "Hard",
            "solution_steps": "Start = 120. Station B = 120 - 45 + 29 = 104. Station C: Half get down, so 104 / 2 = 52 passengers are left.",
            "explanation_description": "Multi-step arithmetic passenger flow."
        },
        {
            "question_text": "How many 3-digit numbers can be formed using the digits 4, 0, and 7 without repeating any digit?",
            "options": ["4", "6", "5", "3"],
            "correct_option": "4",
            "difficulty_level": "Hard",
            "solution_steps": "The digits are 4, 0, 7. A 3-digit number cannot start with 0. The possible starting digits are 4 and 7.\nStarting with 4: 407, 470 (2 numbers).\nStarting with 7: 704, 740 (2 numbers).\nTotal = 4 numbers.",
            "explanation_description": "Permutation with zero constraint."
        },
        {
            "question_text": "What is the sum of the digits of the largest 4-digit number that can be formed using digits 3, 5, 8, 9 (without repetition)?",
            "options": ["25", "26", "24", "23"],
            "correct_option": "25",
            "difficulty_level": "Medium",
            "solution_steps": "The digits are 3, 5, 8, 9. The largest number is 9853. The sum of the digits = 9 + 8 + 5 + 3 = 25.",
            "explanation_description": "Digits manipulation and addition."
        },
        {
            "question_text": "Raju has a piece of wood 3 meters long. He wants to cut it into smaller pieces of 30 cm each. How many cuts must he make to get the desired pieces?",
            "options": ["9", "10", "11", "8"],
            "correct_option": "9",
            "difficulty_level": "Hard",
            "solution_steps": "Total length = 3 meters = 300 cm. Pieces = 300 / 30 = 10 pieces. To get 10 pieces, he needs to make 10 - 1 = 9 cuts.",
            "explanation_description": "Interval logic (cuts vs pieces)."
        },
        {
            "question_text": "Find the mirror image of 'MATH' when the mirror is placed horizontally below the word.",
            "options": ["WATH", "M∀TH (flipped vertically)", "HTAM", "MATH"],
            "correct_option": "M∀TH (flipped vertically)",
            "difficulty_level": "Hard",
            "solution_steps": "Mirror at the bottom flips the letters vertically. M becomes W (flipped), A becomes inverted Ɐ (flipped), T and H flip vertically (T upside down, H remains same). This is represented as M∀TH (flipped vertically).",
            "explanation_description": "Vertical reflection test."
        },
        {
            "question_text": "If ⎔ + ⎔ = 12 and ⎔ * ⎊ = 30, what is the value of ⎊ + ⎊?",
            "options": ["10", "12", "8", "6"],
            "correct_option": "10",
            "difficulty_level": "Medium",
            "solution_steps": "If ⎔ + ⎔ = 12, then ⎔ = 6. Substituting this: 6 * ⎊ = 30 => ⎊ = 5. So, ⎊ + ⎊ = 5 + 5 = 10.",
            "explanation_description": "Symbolic system algebra."
        },
        {
            "question_text": "A pattern has 1 square in the first step, 3 squares in the second step, 5 squares in the third step, and so on. How many squares will be in the 10th step?",
            "options": ["19", "21", "20", "17"],
            "correct_option": "19",
            "difficulty_level": "Hard",
            "solution_steps": "This is an arithmetic sequence of odd numbers: Step n has 2n - 1 squares. For Step 10: 2(10) - 1 = 19 squares.",
            "explanation_description": "Odd number sequence logic."
        },
        {
            "question_text": "Which of the following statement is correct?",
            "options": ["All even numbers end with 5", "The sum of two odd numbers is always even", "The product of any number and 1 is 0", "A circle has 4 corners"],
            "correct_option": "The sum of two odd numbers is always even",
            "difficulty_level": "Medium",
            "solution_steps": "Odd + Odd = Even (e.g., 3 + 5 = 8). So, 'The sum of two odd numbers is always even' is correct.",
            "explanation_description": "Number property validation."
        },
        {
            "question_text": "A shop sells packets of balloons. A packet of 10 balloons costs $8, and a single balloon costs $1. If Kunal wants to buy 34 balloons, what is the minimum money he needs?",
            "options": ["$28", "$26", "$30", "$34"],
            "correct_option": "$28",
            "difficulty_level": "Hard",
            "solution_steps": "Kunal can buy 3 packets of 10 (30 balloons) and 4 single balloons. Cost = 3 * $8 + 4 * $1 = $24 + $4 = $28.",
            "explanation_description": "Everyday optimization arithmetic."
        },
        {
            "question_text": "If ⚂ represents 6 dots, and a cube has 6 faces, what is the total number of dots on 5 identical standard dice?",
            "options": ["105", "110", "90", "120"],
            "correct_option": "105",
            "difficulty_level": "Hard",
            "solution_steps": "Dots on a single standard die = 1 + 2 + 3 + 4 + 5 + 6 = 21 dots. Total dots on 5 dice = 5 * 21 = 105 dots.",
            "explanation_description": "Sum of face values on standard dice."
        },
        {
            "question_text": "A movie ended at 6:10 p.m. If it was 2 hours and 15 minutes long, at what time did the movie start?",
            "options": ["3:55 p.m.", "4:55 p.m.", "3:45 p.m.", "4:00 p.m."],
            "correct_option": "3:55 p.m.",
            "difficulty_level": "Hard",
            "solution_steps": "Subtract 2 hours 15 minutes from 6:10 p.m. Subtracting 2 hours gives 4:10 p.m. Subtracting 15 minutes from 4:10 p.m. gives 3:55 p.m.",
            "explanation_description": "Subtracting elapsed time."
        },
        {
            "question_text": "How many lines of symmetry does a perfect square shape have?",
            "options": ["4", "2", "8", "0"],
            "correct_option": "4",
            "difficulty_level": "Medium",
            "solution_steps": "A perfect square has 4 lines of symmetry: 2 passing through midpoints of opposite sides, and 2 passing through opposite vertices (diagonals).",
            "explanation_description": "Line symmetry geometry."
        },
        {
            "question_text": "In a garden, there are 4 more apple trees than mango trees. If the total number of trees is 24, how many mango trees are there?",
            "options": ["10", "12", "14", "8"],
            "correct_option": "10",
            "difficulty_level": "Hard",
            "solution_steps": "Let mango trees be M. Apple trees = M + 4. Total = M + M + 4 = 24 => 2M = 20 => M = 10. So there are 10 mango trees.",
            "explanation_description": "Word problem algebra."
        }
    ]

def populate_imo_quizzes_direct():
    print("Starting direct IMO Grade 3 quiz population...")
    
    sections = [
        {"name": "Logical Reasoning", "data": get_logical_reasoning()},
        {"name": "Mathematical Reasoning", "data": get_mathematical_reasoning()},
        {"name": "Everyday Mathematics", "data": get_everyday_mathematics()},
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
        existing_meta = supabase_db.table(quiz_table).select("id").eq("board", "CBSE").eq("grade", "Grade 3").eq("subject", "IMO Test").eq("chapter_or_topic", section_name).execute()
        if existing_meta.data:
            existing_id = existing_meta.data[0]["id"]
            print(f"Existing quiz found (ID: {existing_id}). Deleting old questions and quiz...")
            supabase_db.table(question_table).delete().eq(fk_field, existing_id).execute()
            supabase_db.table(quiz_table).delete().eq("id", existing_id).execute()
            
        # Create new quiz row
        quiz_metadata = {
            "board": "CBSE",
            "grade": "Grade 3",
            "subject": "IMO Test",
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
    populate_imo_quizzes_direct()
