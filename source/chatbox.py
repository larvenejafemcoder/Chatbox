from slow_print import *

gpt_name = "PookieGPT"

class Chat:
    def __init__(self, name=gpt_name, delay=(0.03, 0.08)):
        self.name = name
        self.delay = delay

    def chat(self, message):
        slow_print(f"{self.name}: {message}", self.delay)

    def input(self, message):
        return slow_input(f"{self.name}: {message}", self.delay)


'-----------------------------------------------------------------------------------------------------------------------------------'

def general_quest(name=gpt_name):
    health = slow_input(f"{name}:How is your day?\n 1. It's good\n 2. Fine I guess\n 3. Not really good lmao\n").strip()
    if health == "1":
        slow_print("Yay! I'm happy you're doing well.")
    elif health == "2":
        slow_print()("Hmm, neutral vibe... wanna talk more?")
    elif health == "3":
        slow_print("Aww... sending virtual hugs 🫂")
    else:
        slow_print("I couldn't tell how you're feeling, but I'm here anyway.")

bot = Chat(name=gpt_name)