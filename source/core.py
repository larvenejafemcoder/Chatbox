from chatbox import Chat, gpt_name, general_quest, user_name

def main():
    bot = Chat()
    bot.chat(f"Hello! I'm {gpt_name}, your friendly Python chatbot 💬")
    bot.chat("I was written in Python to make you feel at home 🐍💖")

    # Greet user and ask how they're doing
    general_quest()

    # Ask for their name
    user_name()

    # Main loop
    while True:
        choice = input(
            "\nWhat would you like to do next?\n"
            " 1. Talk 💭\n"
            " 2. Ask ❓\n"
            " 3. Quit 👋\n"
            "Your Choice: "
        ).strip()

        if choice == "1":
            general_quest()
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
