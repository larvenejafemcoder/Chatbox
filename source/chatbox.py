from random import choice
import os

from slow_print import slow_input, slow_print
import json

gpt_name = "PookieGPT"



class PookieGPT:
    def __init__(self, name=gpt_name, delay=(0.01, 0.04)):
        self.name = name
        self.delay = delay
        file_path = os.path.join(os.path.dirname(__file__), "responses.json")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.responds = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"[ERROR] Could not load responses.json: {e}")
            self.responds = {}

    # ------------------ Introduction ------------------
    def introduction(self):
        slow_print(f"{self.name}: {choice(self.responds['introduction'])}", self.delay)

    # ------------------ Username Prompt ------------------
    def user_name(self):
        ask_prompt = choice(self.responds['username']['name_asking'])
        username = slow_input(f"{self.name}: {ask_prompt}", self.delay).strip()
        reply_template = choice(self.responds['username']['return_name'])
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

    #------------------------- How Dare you interupt POOKIEGPT ------------------------------#
    def rage_quit(self):
        slow_print(f"{self.name}: {choice(self.responds['rage_quit'])}", self.delay)

    # ------------------ Continue Talking ------------------ #
    def legacy_shutdown(self):
        slow_print(f"{self.name}: {choice(self.responds['shutting_down'])}", self.delay)

    def con_talk(self):
        ask_line = choice(self.responds["talk"])
        continue_talk = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip().lower()

        category_map = {
            "1": "schoolwork_problem",
            "2": "debugging_problem",
            "3": "existential_problem"
        }

        category = category_map.get(continue_talk.strip())

        if continue_talk in category_map:
            slow_print(f"{self.name}: {choice(self.responds[category])}", self.delay)
        else:
            slow_print(f"{self.name}: {choice(self.responds['tryagain'])}", self.delay)
            self.legacy_shutdown()  # Double tap

    # ---------------------- What to do next ------------------------ #

    def whatodo(self):
        ask_line = choice(self.responds["what_to_do"])
        while True:
            whattodonow = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()
            if whattodonow == "1":
                bot.con_talk()
            elif whattodonow == "2":
                slow_print("Sure! What do you wanna talk about? 🗨️")
            elif whattodonow == "3":
                slow_print("Okay, bye bye~ ✨")
                break
            else:
                slow_print(f"{self.name}: {choice(self.responds["tryagain"])}", self.delay)
                break
                    


# ------------------ Initialize Bot ------------------
bot = PookieGPT()
print("chatbox.py loaded successfully!")
