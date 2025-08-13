from chatbox import PookieGPT
import time 



def main():
    bot = PookieGPT()

    bot.introduction() #Introduce thyself
    bot.user_name()      # Ask for name
    bot.general_quest()  # Mood check
    bot.whatodo()
    print("The Programme is running")
    while True:
        time.sleep(1)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        PookieGPT().rage_quit()
