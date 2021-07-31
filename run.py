import random

easy_words = ["able", "acid", "aged", "also", "area", "army"]
medium_words = ["breath", "bridge", "bright", "broken", "budget", "burden"]
hard_words = ["enormous", "entirely", "entrance", "envelope", "equality",
              "equation"]
word = ""

images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

hangman_title = """
  █████   █████
░░███   ░░███
 ░███    ░███   ██████   ████████    ███████ █████████████    ██████   ████████
 ░███████████  ░░░░░███ ░░███░░███  ███░░███░░███░░███░░███  ░░░░░███ ░███░░███
 ░███░░░░░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████ ░███ ░███
 ░███    ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███ ░███ ░███
 █████   █████░░████████ ████ █████░░███████ █████░███ █████░░████████ ████ ███
░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░
                                    ███ ░███
                                   ░░██████
                                    ░░░░░░
"""

print(hangman_title)
print("Welcome to Hangman! Guess all the letters and reveal the word!\n")


def get_word():
    global word
    difficulty = input("Select game difficulty: easy, medium, hard\n")
    if difficulty == "easy":
        word = random.choice(easy_words)
    elif difficulty == "medium":
        word = random.choice(medium_words)
    elif difficulty == "hard":
        word = random.choice(hard_words)
    else:
        print("Input not valid, please select a valid option")
        get_word()
    return word
        

def main():
    get_word()
    print(word)


main()
