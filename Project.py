# Python Quiz Application

def display_welcome_message():
    print("=======================================")
    print("  Welcome to the Ultimate Quiz Game!  ")
    print("  Test your knowledge and have fun!   ")
    print("=======================================\n")

def display_thank_you_message():
    print("=======================================")
    print("  Thank you for taking the quiz!  ")
    print("  We hope you enjoyed it!   ")
    print("=======================================")

def ask_question(question, options, correct_answer):
    print(f"{question}")
    for option in options:
        print(option)
    user_answer = input("Enter your answer (1, 2, 3, or 4): ").strip()
    
    # Validate input
    while user_answer not in ['1', '2', '3', '4']:
        print("Invalid input. Please select 1, 2, 3, or 4.")
        user_answer = input("Enter your answer (1, 2, 3, or 4): ").strip()
    
    return user_answer == correct_answer

def calculate_score(correct_answers):
    return correct_answers

def display_results(score, total_questions):
    print("\n=======================================")
    print(f"Your final score is {score}/{total_questions}.")
    
    # Performance Message
    if score == total_questions:
        print("Excellent! You got all the answers correct!")
    elif score >= total_questions / 2:
        print("Good job! You got more than half of the answers correct!")
    else:
        print("Keep trying! You can improve with more practice!")
    print("=======================================\n")

def run_quiz():
    display_welcome_message()
    
    quiz = [
        {
            "question": "What is the capital of France?",
            "options": ["1) Berlin", "2) Madrid", "3) Paris", "4) Rome"],
            "answer": "3"
        },
        {
            "question": "Which language is primarily used for web development?",
            "options": ["1) Python", "2) Java", "3) JavaScript", "4) C++"],
            "answer": "3"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["1) 1", "2) 2", "3) 3", "4) 5"],
            "answer": "2"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["1) William Wordsworth", "2) Charles Dickens", "3) William Shakespeare", "4) Mark Twain"],
            "answer": "3"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1) Earth", "2) Venus", "3) Mars", "4) Jupiter"],
            "answer": "3"
        }
    ]
    
    correct_answers = 0
    
    for q in quiz:
        if ask_question(q['question'], q['options'], q['answer']):
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.\n")
    
    score = calculate_score(correct_answers)
    display_results(score, len(quiz))
    display_thank_you_message()

if __name__ == "__main__":
    run_quiz()
