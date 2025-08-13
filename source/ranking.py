import json
import hashlib

class RankingSystem:
    USERS_FILE = "users.json"
    RANKS_FILE = "ranksystem.json"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # ---------------- USERS ----------------
    @staticmethod
    def load_users():
        try:
            with open(RankingSystem.USERS_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_users(users):
        with open(RankingSystem.USERS_FILE, "w") as f:
            json.dump(users, f, indent=2)

    # ---------------- RANKS ----------------
    @staticmethod
    def load_ranks():
        try:
            with open(RankingSystem.RANKS_FILE, "r") as f:
                return json.load(f)["RANKS"]
        except FileNotFoundError:
            return []

    # ---------------- AUTH LOGIC ----------------
    @staticmethod
    def register(username, password):
        users = RankingSystem.load_users()
        if username in users:
            return False, "Username already exists!"
        users[username] = {
            "password": RankingSystem.hash_password(password),
            "score": 0,
            "rank": "Recruit"
        }
        RankingSystem.save_users(users)
        return True, "Registration successful!"

    @staticmethod
    def login(username, password):
        users = RankingSystem.load_users()
        if username not in users:
            return False, "User not found!"
        if users[username]["password"] != RankingSystem.hash_password(password):
            return False, "Invalid password!"
        return True, "Login successful!"


# -------------- TESTING --------------
if __name__ == "__main__":
    print("Loading rank thresholds...")
    print(RankingSystem.load_ranks())

    print("\nRegistering 'Finley'...")
    print(RankingSystem.register("Finley", "password123"))

    print("\nTrying wrong login...")
    print(RankingSystem.login("Finley", "wrongpass"))

    print("\nTrying correct login...")
    print(RankingSystem.login("Finley", "password123"))

    print("\nCurrent users file content:")
    print(RankingSystem.load_users())
    print(RankingSystem.load_users())