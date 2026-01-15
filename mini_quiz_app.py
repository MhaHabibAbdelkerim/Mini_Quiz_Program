import random
# Mini Quiz App 


# Track the Score and total questions
score = 0
total_questions = 0

# Question Data
questions = [
    {"question": "What is the capital of France?", "answer": "Paris", "difficulty": "easy"},
    {"question": "What library is used to generate random numbers in Python?", "answer": "random", "difficulty": "easy"},
    {"question": "What is the correct file extension for Python files?", "answer": ".py", "difficulty": "easy"},
    {"question": "Which keyword is used to define a function in Python?", "answer": "def", "difficulty": "easy"},
    {"question": "What does the len() function do in Python?", "answer": "Returns the length of an object", "difficulty": "easy"},
    {"question": "What does break do inside a loop?", "answer": "Exits the loop", "difficulty": "easy"},
    {"question": "What keyword is used to create a loop that iterates over a sequence?", "answer": "for", "difficulty": "easy"},
    {"question": "Which function is used to get user input in Python?", "answer": "input", "difficulty": "easy"},
    {"question": "Which operator is used for exponentiation?", "answer": "**", "difficulty": "easy"},
    {"question": "What symbol is used to start a comment in Python?", "answer": "#", "difficulty": "easy"},
    {"question": "Which keyword stops a loop immediately?", "answer": "break", "difficulty": "easy"},
    {"question": "Which keyword skips the current iteration of a loop?", "answer": "continue", "difficulty": "easy"},
    {"question": "What keyword is used to define a class?", "answer": "class", "difficulty": "easy"},
    {"question": "What function converts a string to an integer?", "answer": "int", "difficulty": "easy"},
    {"question": "What does len([1, 2, 3]) return?", "answer": "3", "difficulty": "easy"},
    {"question": "Which data type is used to store key-value pairs?", "answer": "dictionary", "difficulty": "easy"},
    {"question": "What keyword is used to return a value from a function?", "answer": "return", "difficulty": "easy"},
    {"question": "Which operator checks for equality?", "answer": "==", "difficulty": "easy"},
    {"question": "Which keyword is used to import a module?", "answer": "import", "difficulty": "easy"},
    {"question": "What function is used to find the maximum value in a list?", "answer": "max", "difficulty": "easy"},
    {"question": "What function is used to find the minimum value in a list?", "answer": "min", "difficulty": "easy"},
    {"question": "Which keyword is used to check a condition?", "answer": "if", "difficulty": "easy"},
    {"question": "Which function converts a value to a string?", "answer": "str", "difficulty": "easy"},
    {"question": "What does list.append() do?", "answer": "Adds an element to the list", "difficulty": "easy"},
    {"question": "What will print(type(5)) output?", "answer": "<class 'int'>", "difficulty": "medium"},
    {"question": "Which Data Structure is mutable: List, Tuple, or String?", "answer": "List", "difficulty": "medium"},
    {"question": "What Keyword is used to handle exceptions in Python?", "answer": "try", "difficulty": "medium"},
    {"question": "Which library is commonly used for data manipulation in Python?", "answer": "pandas", "difficulty": "medium"},
    {"question": "What data type is returned by input()?", "answer": "string", "difficulty": "medium"},
    {"question": "Which data type is immutable: list or tuple?", "answer": "tuple", "difficulty": "medium"},
    {"question": "Which keyword is used to define an anonymous function?", "answer": "lambda", "difficulty": "medium"},
    {"question": "Which keyword is used to handle exceptions after try?", "answer": "except", "difficulty": "medium"},
    {"question": "What will this output? print(3 == 3 and 2 > 5)", "answer": "False", "difficulty": "hard"},
    {"question": "What is the output of: range(1, 10, 2) converted to a list?", "answer": "[1, 3, 5, 7, 9]", "difficulty": "hard"},
    {"question": "What is the result of 10 // 3?", "answer": "3", "difficulty": "hard"},
    {"question": "What does bool(0) return?", "answer": "False", "difficulty": "hard"},
    {"question": "What does type(True) return?", "answer": "<class 'bool'>", "difficulty": "hard"},
    {"question": "What does range(5) produce?", "answer": "0 to 4", "difficulty": "hard"},
    {"question": "What is the output of len('Python')?", "answer": "6", "difficulty": "hard"},
    {"question": "What does isinstance(5, int) return?", "answer": "True", "difficulty": "hard"}
]

# Ask the User to choose difficulty or choose random order
difficulty = input("Choose difficulty (easy, medium, hard) to start the quiz: ").strip().lower()

#Filter questions based on difficulty ir shuffle all for random
if difficulty not in ["easy", "medium", "hard"]:
       random.shuffle(questions)
       filtered_questions = questions
else:
       filtered_questions = [q for q in questions if q["difficulty"] == difficulty]

# Quiz Loop     
for q in filtered_questions:
    total_questions += 1
    user_input = input(q["question"] + " ")
    if user_input.strip().lower() == q["answer"].strip().lower():
            score += 1
            print("Correct!")
    else:
            print(f"Wrong! The correct answer is: {q['answer']}")
    print()

# Final Score
print(f"Quiz Over! Your final score is {score} out of {total_questions}.")
percentage = (score / total_questions) * 100
print(f"Your percentage score is: {percentage:.2f}%")


