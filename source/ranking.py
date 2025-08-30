import json                      # Built-in JSON parser/serializer for reading/writing .json files
from slow_print import *         # Imports your custom slow_print() (prints text character-by-character, presumably)
import hashlib                   # For hashing passwords (SHA-256 below)

class RankingSystem:             # Namespaced container for all your ranking/auth helpers
    USERS_FILE = "ranksystem.json"  # File path used for *users* storage (⚠ currently same as ranks file)
    RANKS_FILE = "ranksystem.json"  # File path used for *rank thresholds* (⚠ same file as above)

    @staticmethod
    def hash_password(password):    # Utility: convert plain text password -> SHA-256 hex digest
        return hashlib.sha256(password.encode()).hexdigest()

    # ---------------- USERS ----------------
    @staticmethod
    def load_users():               # Load users dict from USERS_FILE
        try:
            with open(RankingSystem.USERS_FILE, "r") as f:  # Open JSON file for reading
                return json.load(f)                         # Parse and return the entire JSON as a Python dict
        except FileNotFoundError:                           # If file doesn’t exist yet…
            return {}                                       # …start with an empty users dict

    @staticmethod
    def save_users(users):          # Persist users dict back to USERS_FILE
        with open(RankingSystem.USERS_FILE, "w") as f:      # Open JSON file for writing (truncate/overwrite)
            json.dump(users, f, indent=2)                   # Serialize pretty-printed JSON

    # ---------------- RANKS ----------------
    @staticmethod
    def load_ranks():               # Load rank thresholds from RANKS_FILE
        try:
            with open(RankingSystem.RANKS_FILE, "r") as f:  # Open the same JSON file (⚠ same file as users)
                return json.load(f)["RANKS"]                # Return value under "RANKS" key (⚠ KeyError if missing)
        except FileNotFoundError:                           # If file not found…
            return []                                       # …return empty list of ranks

    # ---------------- AUTH LOGIC ----------------
    @staticmethod
    def register(username, password):   # Create a new user entry
        users = RankingSystem.load_users()                  # Load current users (actually the *whole* JSON file)
        if username in users:                               # If username key already exists…
            return False, slow_print("Username already exists!")  # Print message via slow_print AND return tuple
        users[username] = {                                 # Create a user record at key 'username'
            "password": RankingSystem.hash_password(password), # Store *hashed* password
            "score": 0,                                     # Start with 0 points
            "rank": "Recruit"                               # Default starting rank
        }
        RankingSystem.save_users(users)                     # Write updated dict back to disk
        return True, slow_print("Registration successful!") # Print success message & return tuple

    @staticmethod
    def login(username, password):      # Validate credentials for an existing user
        users = RankingSystem.load_users()                  # Load users (again, full JSON)
        if username not in users:                           # If user not found…
            return False, slow_print("User not found!")                 # Return failure + message (not slow_print here)
        if users[username]["password"] != RankingSystem.hash_password(password):  # Compare hashes
            return False, "Invalid password!"               # Wrong password
        return True, slow_print("Login successful!")                    # Auth OK


    # -------------- TESTED -------------- #
    # slow_print("Loading rank thresholds...")                # Slowly print a header line
    # slow_print(RankingSystem.load_ranks())                  # Slowly print the ranks list (or [])

    # slow_print("\nRegistering 'Finley'...")                 # Header for registration test
    # slow_print(RankingSystem.register("Finley", "password123"))  # Call register; then slow_print the *tuple* it returns

    # slow_print("\nTrying wrong login...")                   # Header for a failed login test
    # slow_print(RankingSystem.login("Finley", "wrongpass"))  # Call login (wrong pass); slow_print the returned tuple

    # slow_print("\nTrying correct login...")                 # Header for a successful login test
    # slow_print(RankingSystem.login("Finley", "password123"))# Call login (correct pass); slow_print the returned tuple

    # slow_print("\nCurrent users file content:")             # Header for dumping users
    # slow_print(RankingSystem.load_users())                  # Print the whole JSON dict as a Python object (stringified)
    # slow_print(RankingSystem.load_users())                  # Print it again (duplicate output on purpose)


    @staticmethod
    def registeringUserRank(): # made this since there is no way of inputting user on the terminal 
        rank = RankingSystem() #replace RankingSystem() with rank placeholder
        rank.load_ranks() #proceeds to read the json input of ranksystem.json 

        user_name = slow_input("Register your username for rankingsytem: ") #ask for user_ranking_registration

        # Then ask for password
        user_password = slow_input("What password do you want to set? ") # then proceeds to ask for password also

        # Register password with rank
        
        registered = rank.register(user_name, user_password) #same for load_ranks() but inject the inputs back to the file

        slow_print("Welcome Aboard! You are now Comrade {user_name}!")
        return registered #successfully injected 

    @staticmethod
    def loggingInToUserRank(): # the same for registering but for loggin in 
        rank = RankingSystem() #also the same 
        rank.load_ranks()

        user_name = slow_input("Hello, welcome back: ")

        #Then also ask for password

        user_password = slow_input(f"Hello {user_name}, please enter your password: ")

        logging_in = rank.login(user_name, user_password) #instead of injecting we take what is available in ranksystem.json and logging for user 

        slow_print(f"Welcome back! Comrade {user_name}!")
        return logging_in

    # -------- Wrapper Function for Login -------- #
    @staticmethod
    def userInitLogin():
        slow_print("Welcome to the Ranking System!")
        choice = slow_input("Do you want to (R)egister or (L)ogin? ").strip().lower()

        if choice.startswith("r"):
            success, msg = RankingSystem.registeringUserRank()
            return success, msg
        elif choice.startswith("l"):
            success, msg = RankingSystem.loggingInToUserRank()
            return success, msg
        else:
            return False, "Invalid choice!"


