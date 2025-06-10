QUIZ = [
    {
        'question': "Which planet is known as the Red Planet?",
        'answer': "Mars",
        'options': ["Earth", "Mars", "Jupiter", "Mercury"]
    },
    {
        'question': "What is the capital city of Japan?",
        'answer': "Tokyo",
        'options': ["Seoul", "Tokyo", "Beijing", "Bangkok"]
    },
    {
        'question': "Who wrote the play 'Romeo and Juliet'?",
        'answer': "William Shakespeare",
        'options': ["William Shakespeare", "Jane Austen", "Mark Twain", "Charles Dickens"]
    },
    {
        'question': "What is the powerhouse of the cell?",
        'answer': "Mitochondria",
        'options': ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"]
    },
    {
        'question': "Which element has the chemical symbol 'O'?",
        'answer': "Oxygen",
        'options': ["Gold", "Oxygen", "Osmium", "Oganesson"]
    },
    {
        'question': "In which year did the Titanic sink?",
        'answer': "1912",
        'options': ["1905", "1912", "1920", "1898"]
    },
    {
        'question': "What is the largest ocean on Earth?",
        'answer': "Pacific Ocean",
        'options': ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"]
    },
    {
        'question': "Who painted the Mona Lisa?",
        'answer': "Leonardo da Vinci",
        'options': ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"]
    },
    {
        'question': "What is the freezing point of water in Celsius?",
        'answer': "0",
        'options': ["-32", "0", "100", "32"]
    },
    {
        'question': "Which country gifted the Statue of Liberty to the USA?",
        'answer': "France",
        'options': ["United Kingdom", "Germany", "France", "Italy"]
    }
]



def quiz(questions):
    score = 0
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
    

quiz(QUIZ)