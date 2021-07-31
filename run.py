import random
import os
from images import images, hangman_title


easy_words = ["able", "acid", "aged", "also", "area", "army"]
medium_words = ["breath", "bridge", "bright", "broken", "budget", "burden"]
hard_words = ["enormous", "entirely", "entrance", "envelope", "equality",
              "equation"]
lives = 7
guessed = []
missed = []
game_complete = False
word = ""


def get_word():
    global word
    difficulty = input("Select game difficulty: easy, medium, hard:\n")
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


def show_status(word):
    os.system("clear")
    print(images[7-lives])
    print(len(word) * "_ ")


def play():
    global game_complete
    while game_complete is False:
        guess = input("Guess a letter or the entire word: \n").upper()
        if guess == word:
            game_complete = True
            print("Congratulations")
        elif guess in word:
            print(f"Well done, {guess} is part of the word")
        else:
            print("You lost")


def main():
    print(hangman_title)
    print("Welcome to Hangman! Guess all the letters and reveal the word!\n")
    word = get_word()
    show_status(word)
    play()


main()
