from http.client import responses
from random import choice
from slow_print import *  # Assuming slow_print and slow_input are defined in here
import json
import random

gpt_name = "PookieGPT"
name = gpt_name

class Chat:
    def __init__(self, delay=(0.03, 0.08)):
        self.name = name
        self.delay = delay

    def chat(self, message):
        slow_print(f"{self.name}: {message}", self.delay)

    def input(self, message):
        return slow_input(f"{self.name}: {message}", self.delay)


# ------------------ Load JSON ------------------
with open("responses.json", "r", encoding="utf-8") as f:
    responds = json.load(f)

# ------------------ Username Prompt ------------------
def user_name():
    username = slow_input(f"{name}: Hello! {random.choice(responds['usrname']['nameasking'])}").strip()
    template = random.choice(responds['usrname']['returnname'])
    message = template.format(username=username)
    slow_print(f"{name}: {message}")

# ------------------ General Question ------------------
def general_quest():
    prompt = random.choice(responds["greeting"])
    mood = slow_input(prompt + "\nYour Choice: ").strip().lower()

    if mood == "1":
        slow_print(random.choice(responds["health_responses"]["1"]))
    elif mood == "2":
        slow_print(random.choice(responds["health_responses"]["2"]))  # This one is a single string
    elif mood == "3":
        slow_print(random.choice(responds["health_responses"]["3"]))
    elif "sad" in mood or "bad" in mood:
        slow_print(random.choice(responds["health_responses"]["2"]))
    else:
        slow_print("I couldn't tell how you're feeling, but I'm here anyway.")

# ------------------ Continue Talking ------------------

def con_talk():
    contalk = slow_input(f"{name}: Okay! {random.choice(responds['talk'])} \n") # "Spill it. What’s going on?"
    if contalk == "1":
        slow_print("Oh School World? What is bugging my pookie rn?")

# ------------------ Initialize Bot ------------------
bot = Chat()
