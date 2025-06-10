from prompt import *
while True:
    user_input = input("You:    ").strip().lower()
    reply = get_prompt(user_input)

    