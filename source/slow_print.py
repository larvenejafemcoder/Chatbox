import time
import random

def slow_print(text, delay_range=(0.01, 0.08)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()

def slow_input(prompt, delay_range=(0.01, 0.08)):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    return input()

'''okay so define a function already with slow input
func(parsing parameter =>> prompt for message, and delay_time(parsing 0.01(the speed), and 0.08(the time when text should be completed) ) ) 
    then we made a for loop
    
    # Loop through every character in the string
    for character in text(or:prompt):
        print(each char, end with "", then make the flush effect) #   print without newline, flush so it shows immediately
        we imported the library so we gon use it    # wait randomly between min and max delay
        time.sleep(random.uniform(delaytime))     # print newline after full message
'''