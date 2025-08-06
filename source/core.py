from chatbox import Chat, gpt_name, general_quest, user_name, con_talk
from source.slow_print import slow_input


def main():
    bot = Chat()
    bot.chat(f"Hello! I'm {gpt_name}, your friendly Python chatbot 💬") #1
    bot.chat("I was written in Python to make you feel at home 🐍💖") #2


    # Ask for their name
    user_name() #2
    # Greet user and ask how they're doing
    general_quest() #3

    # Main loop
    while True:
        choice = slow_input(
            "\nWhat would you like to do next?\n"
            " 1. Continue talking 💭\n"
            " 2. Ask me a question ❓\n"
            " 3. Quit now! 👋\n"
            "Your Choice: "
        ).strip()

        if choice == "1": #Continue talking
            con_talk()
        elif choice == "2":
            print("Sure! What do you wanna talk about? 🗨️")
        elif choice == "3":
            print("Okay, bye bye~ ✨")
            break
        else:
            print("I didn't understand that... try 1, 2, or 3 💬")
            break

if __name__ == '__main__':
    main()
