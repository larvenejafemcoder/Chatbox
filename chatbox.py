from slow_print import slow_print

class Chat:
    def __init__(self, name="ChatBox", delay=(0.03, 0.08)):
        self.name = name
        self.delay = delay

    def chat(self, message):
        slow_print(f"{self.name}: {message}", self.delay)


gpt_name = "PookieGPT"
bot = Chat(name=gpt_name)