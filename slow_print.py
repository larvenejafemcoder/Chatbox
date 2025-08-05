import time
import random

def slow_print(text, delay_range=(0.03, 0.08)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()
