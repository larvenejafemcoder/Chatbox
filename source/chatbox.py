from random import choice  # Randomly select items from lists (for varied responses)
import os  # File path manipulation
from slow_print import slow_input, slow_print  # Custom slow typing/printing functions
import json  # For loading bot responses from JSON

gpt_name = "PookieGPT"  # Default bot name (cute but dangerous)


# ------------------ Bot Class ------------------ #
class PookieGPT:
    def __init__(self, name=gpt_name, delay=(0.01, 0.04)):
        self.name = name  # Name of the bot (default = "PookieGPT")
        self.delay = delay  # Typing delay range for slow_print

        # Build file path to responses.json in same folder as this script
        file_path = os.path.join(os.path.dirname(__file__), "responses.json")

        # Try to load responses.json
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.responds = json.load(f)  # Load Dictionary with all response categories
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"[ERROR] Could not load responses.json: {e}")  # Show error if file missing or broken
            self.responds = {}  # Avoid crashing—fallback to empty dict

    # ------------------ Introduction ------------------ #
    def introduction(self):
        # Picks a random intro line from JSON, prints it slowly
        slow_print(f"{self.name}: {choice(self.responds['introduction'])}", self.delay)

    # ------------------ Username Prompt ------------------ #
    def user_name(self):
        # Ask for user's name with a random prompt from JSON
        ask_prompt = choice(self.responds['username']['name_asking'])
        username = slow_input(f"{self.name}: {ask_prompt}", self.delay).strip()

        # Pick a random reply template and insert username
        reply_template = choice(self.responds['username']['return_name'])
        slow_print(f"{self.name}: {reply_template.format(username=username)}", self.delay)

    # ------------------ General Question ------------------ #
    def general_quest(self):
        # Start conversation with a greeting from JSON
        prompt = choice(self.responds["greeting"])
        mood = slow_input(f"{self.name}: {prompt}\nYour Choice: ", self.delay).strip().lower()

        # Check mood choice and pick response from JSON categories
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

    # ------------------ RAGE QUIT MODE ------------------ #
    def rage_quit(self):
        slow_print(f"{self.name}: {choice(self.responds['rage_quit'])}", self.delay)

    # ------------------ LEGACY SHUTDOWN ------------------ #
    def legacy_shutdown(self):
        slow_print(f"{self.name}: {choice(self.responds['shutting_down'])}", self.delay)

    # ------------------ Continue Talking ------------------ #
    def con_talk(self):
        ask_line = choice(self.responds["talk"])
        continue_talk = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip().lower()

        # Maps menu choice numbers to JSON categories
        category_map = {
            "1": "schoolwork_problem",
            "2": "debugging_problem",
            "3": "existential_problem"
        }

        category = category_map.get(continue_talk.strip())

        if continue_talk in category_map:
            # Respond from the chosen category
            slow_print(f"{self.name}: {choice(self.responds[category])}", self.delay)
        else:
            # Invalid choice → ask to try again
            slow_print(f"{self.name}: {choice(self.responds['tryagain'])}", self.delay)
            self.legacy_shutdown()  # Dramatic exit

    # ------------------ What to do next ------------------ #
    def whatodo(self):
        ask_line = choice(self.responds["what_to_do"])
        while True:
            whattodonow = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()
            if whattodonow == "1":
                bot.con_talk()  # Continue talking
            elif whattodonow == "2":
                slow_print("Sure! What do you wanna talk about? 🗨️")
            elif whattodonow == "3":
                slow_print("Okay, bye bye~ ✨")  # Graceful exit
                break
            else:
                break


# ------------------ Initialize Bot ------------------ #
bot = PookieGPT()
print("chatbox.py loaded successfully!")  # Confirmation on import/run
