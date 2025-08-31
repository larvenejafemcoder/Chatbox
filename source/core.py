#!/usr/bin/env python3

from chatbox import PookieGPT
from ranking import *
import time 



def main():
    #bot = PookieGPT()   # make a chatbot instance

    #bot.introduction()  # bot says hello
    #bot.user_name()     # bot asks your name
    #bot.general_quest() # bot checks your mood
    #bot.whatodo()       # bot asks what you wanna do next   

    RankingSystem.userInitLogin()
    
 
    while True:         # endless loop
        time.sleep(1)   # but it just sleeps, doesn’t do anything
        




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        PookieGPT().rage_quit()


