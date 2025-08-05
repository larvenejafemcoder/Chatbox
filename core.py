from chatbox import Chat
from chatbox import general_quest
from chatbox import gpt_name


if __name__ == '__main__':
    bot = Chat(name=gpt_name)
    bot.chat(f"Hello I am a chatbot named {gpt_name}, how can I help u!")
    bot.chat("I was written in Python to make you feel at home.")

general_quest()

def user_name():
    username = input("Okay! What is your name?\nMy name is: ")
    print("Okay, hello", username + "!")

# Main loop
while True:
    continue_now = input("\nWhat would you wanna do?\n 1. Talk\n 2. Ask\n 3. Quit\n")
    if continue_now == "1":
        general_quest()
        user_name()
    elif continue_now == "2":
        print("Sure! What do you wanna talk about?")
    elif continue_now == "3":
        print("Okay, bye bye~")
        break  # use break instead of quit() so the program ends cleanly
    else:
        print("I didn't understand that... try 1, 2, or 3 💬")
        break
