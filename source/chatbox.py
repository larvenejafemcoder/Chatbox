from random import choice  # Randomly select items from lists (for varied responses)
import os  # File path manipulation
from slow_print import slow_input, slow_print  # Custom slow typing/printing functions
from ranking import RankingSystem
import json  # For loading bot responses from JSON

gpt_name = "PookieGPT"  # Default bot name (cute but dangerous)
dev_name = "Larvene Jafem" #Default Dev's Project owner name

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
    def introduction(self,username):
        # Picks a random intro line from JSON, prints it slowly
        slow_print(f"{self.name}: {choice(self.responds['introduction'])}", self.delay)
        slow_print(f"Hey boss, my name is PookieGPT!")

    # ------------------ General Question ------------------ #
    def general_quest(self):
        # Asks mood
        mood = slow_input(f"{self.name}: {choice(self.responds['greeting'])}", self.delay).strip()
        mood_map = {"1": "1", "2": "2", "3": "3"}
        key = mood_map.get(mood)

        # Basic keyword detection
        if not key and ("sad" in mood or "bad" in mood):
            key = "2"

        if key:
            response = choice(self.responds["health_responses"][key])
        else:
            response = "I couldn't tell how you're feeling, but I'm here anyway. 🌸"

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
        continue_talk = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()

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


    def askmeQuestion(self):
        user_q = slow_input(f"{self.name}: {choice(self.responds['askPookie'])}", self.delay).strip()

        # Simple mapping for demonstration
        '''
        question_map = {
            "1": "whatimfor",
            "2": "howispookie",
            "3": "tellajoke",
            "4": "whatslarvesjob",
            "5": "whymentalissue",
            "6": "staterankcommissioner"
            }
        '''
        #Iterate throught the question map and print the response
        match (user_q):
            case "1":
                slow_print(f"{self.name}: {choice(self.responds['whatimfor'])}")
            case "2":
                slow_print(f"{self.name}: {choice(self.responds['howispookie'])}")
            case "3":
                slow_print(f"{self.name}: {choice(self.responds['jokes'])}")
            case "4":
                slow_print(f"{dev_name}: {choice(self.responds['whatslarvesjob'])}") #what is Larve's JOB?
            case "5":
                slow_print(f"{dev_name}: {choice(self.responds['whymentalissue'])}") #why is Larve having mental issues?
            case "6":
                slow_print(f"{self.name}: {choice(self.responds['staterankcommissioner'])}") #who even is Larve?
            case _:
                slow_print(f"{self.name}: {choice(self.responds['tryagain'])}")



        # ------------------ What to do next ------------------ #
    def whatodo(self):
        ask_line = choice(self.responds["what_to_do"])
        while True:
            whattodonow = slow_input(f"{self.name}: {ask_line}\n", self.delay).strip()
            if whattodonow == "1":
                bot.con_talk()  # Continue talking
            elif whattodonow == "2":
                bot.askmeQuestion() #slow_print("Sure! What do you wanna ask me about? 🗨️")
            elif whattodonow == "3":
                slow_print(f"{self.name}: {choice(self.responds['goodbye'])}", self.delay)  # Graceful exit
                break
            else:
                break


# ------------------ Initialize Bot ------------------ #
bot = PookieGPT()
print("chatbox.py loaded successfully!")  # Confirmation on import/run
