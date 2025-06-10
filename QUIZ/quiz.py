from quizQ import quizQ
import random

def quiz(questions, num_questions=None):
    score = 0
    random.shuffle(questions)
    if num_questions:
        questions = questions[:num_questions]
    for q_quest in questions:
        print(f"\n{q_quest['question']}")
        for i , option in enumerate(q_quest['options']):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_ans = int(input("Enter the answer (1-4):\t"))
                if 1 <= user_ans < len(q_quest['options']):
                    user_selected_ans = q_quest['options'][user_ans - 1]
                    break
                else:
                    print("Please Try Again.")
            except ValueError:
                print("Value is error")
        
        if user_selected_ans.lower() == q_quest['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Wrong!!!, The correct answer was {q_quest['answer']}")
    print(f"Game Finished !! You Got {score} out of {len(questions)} question correct")
    

quiz(quizQ, num_questions=10)