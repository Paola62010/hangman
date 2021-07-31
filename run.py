import random

easy_words = ["able", "acid", "aged", "also", "area", "army"]
medium_words = ["breath", "bridge", "bright", "broken", "budget", "burden"]
hard_words = ["enormous", "entirely", "entrance", "envelope", "equality", 
              "equation"]

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
 ░███████████  ░░░░░███ ░░███░░███  ███░░███░░███░░███░░███  ░░░░░███ ░░███░░███ 
 ░███░░░░░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████  ░███ ░███ 
 ░███    ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███ ░███ 
 █████   █████░░████████ ████ █████░░███████ █████░███ █████░░████████ ████ █████
░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░ 
                                    ███ ░███
                                   ░░██████
                                    ░░░░░░
"""

print(hangman_title)
print(images[6])
hangman_title.rstrip()
