#!/usr/bin/env python3

from chatbox import *
import time 

def main():
    # login once
    login_ok, username = RankingSystem.userInitLogin()

    time.sleep(1)
    bot = PookieGPT()

    bot.introduction(username)
    bot.general_quest()
    bot.whatodo()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        PookieGPT().rage_quit()
