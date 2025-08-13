import time                      # Used for adding delays (pausing between characters)
import random                    # Used for picking a random delay each time

# ------------------ Slow Print Function ------------------ #
def slow_print(text, delay_range=(0.01, 0.06)):
    """
    Prints text character-by-character with a random delay between each.
    delay_range: tuple(min_delay, max_delay) in seconds.
    """

    # Loop through every character in the given text
    for char in text:
        print(char, end='', flush=True)           # Print each char without newline, flush so it appears instantly
        time.sleep(random.uniform(*delay_range))  # Wait for a random time between min and max delay
    print()                                       # After finishing, print a newline

# ------------------ Slow Input Function ------------------ #
def slow_input(prompt, delay_range=(0.01, 0.06)):
    """
    Displays a prompt slowly (like typing), then waits for user input.
    delay_range: tuple(min_delay, max_delay) in seconds.
    """

    # Loop through every character in the prompt string
    for char in prompt:
        print(char, end='', flush=True)           # Print one char at a time, without newline
        time.sleep(random.uniform(*delay_range))  # Random pause for "human typing" effect
    return input()                                # After prompt is done, wait for user to type their answer
