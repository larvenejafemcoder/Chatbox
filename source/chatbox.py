from random import choice
from slow_print import slow_input, slow_print
import json

gpt_name = "PookieGPT"



class PookieGPT:
    def __init__(self, name=gpt_name, delay=(0.01, 0.06)):
        self.name = name
        self.delay = delay
        with open("responses.json", "r", encoding="utf-8") as f:
            self.responds = json.load(f)

    # ------------------ Introduction ------------------
    def intro(self):
        slow_print(f"{self.name}: {choice(self.responds['introduction'])}", self.delay)

    # ------------------ Username Prompt ------------------
    def user_name(self):
        ask_prompt = choice(self.responds['usrname']['nameasking'])
        username = slow_input(f"{self.name}: {ask_prompt}", self.delay).strip()
        reply_template = choice(self.responds['usrname']['returnname'])
        slow_print(f"{self.name}: {reply_template.format(username=username)}", self.delay)

    # ------------------ General Question ------------------
    def general_quest(self):
        prompt = choice(self.responds["greeting"])
        mood = slow_input(f"{self.name}: {prompt}\nYour Choice: ", self.delay).strip().lower()

        if mood == "1":
            response = choice(self.responds["health_responses"]["1"])
        elif mood == "2":
            response = choice(self.responds["health_responses"]["2"])
        elif mood == "3":
            response = choice(self.responds["health_responses"]["3"])
        elif "sad" in mood or "bad" in mood:
            response = choice(self.responds["health_responses"]["2"])
        else:
            response = "I couldn't tell how you're feeling, but I'm here anyway."

        slow_print(f"{self.name}: {response}", self.delay)

    #-------------------------------------------------------
    def interupt_quit(self):
        slow_print(f"{self.name}: {choice(self.responds['ragequit'])}", self.delay)

    # ------------------ Continue Talking ------------------
    def con_talk(self):
        ask_line = choice(self.responds["talk"])
        contalk = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()
        if contalk == "1":
            slow_print(f"{self.name}: Oh School World? What is bugging my pookie rn?", self.delay)
            
    def whatodo(self):
        ask_line = choice(self.responds["whattodo"])
        while True:
            whadado = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()
            if whadado == "1":
                bot.con_talk()
            elif whadado == "2":
                slow_print("Sure! What do you wanna talk about? 🗨️")
            elif whadado == "3":
                slow_print("Okay, bye bye~ ✨")
                break
            else:
                slow_print("I didn't understand that... try 1, 2, or 3 💬")
                break
                    
            
    # while True:
    # choice = bot(
    #     "\nWhat would you like to do next?\n"
    #     " 1. Continue talking 💭\n"
    #     " 2. Ask me a question ❓\n"
    #     " 3. Quit now! 👋\n"
    #     "Your Choice: "
    # ).strip()

    # if choice == "1":
    #     bot.con_talk()
    # elif choice == "2":
    #     bot.chat("Sure! What do you wanna talk about? 🗨️")
    # elif choice == "3":
    #     bot.chat("Okay, bye bye~ ✨")
    #     time.sleep(1)
    #     break
    # else:
    #     bot.chat("I didn't understand that... try 1, 2, or 3 💬")
    #     break

# ------------------ Initialize Bot ------------------
bot = PookieGPT()
print("chatbox.py loaded successfully!")
