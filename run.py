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
word = "able"


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
    
    global guessed
    global missed
    global lives
    global game_complete
    while game_complete is False and lives > 0:
        guess = input("Guess a letter or the entire word: \n").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in word and len(guessed) != len(word):
                print(f"Well done, {guess} is part of the word.")
                guessed.append(guess)
                print(f"Missed: {missed}")
                print(f"Lives remaining: {lives}")
            elif guess in word and len(guessed) == len(word):
                print("Congratularions, you guessed the word")
                game_complete = True
            elif guess not in word and lives != 1:
                print(f"Sorry, {guess} is not part of the word. Try again.")
                missed.append(guess)
                lives -= 1
                print(f"Missed: {missed}")
                print(f"Lives remaining: {lives}")
            else:
                print(f"Sorry, the correct word was {word}")
                game_complete = True
        elif guess == word and guess.isalpha():
            if guess == word:
                print("Congratulations! You guessed the word!")
                game_complete = True
        elif guess != word:
            print(f"Sorry, {guess} is not the correct word")
            lives -= 1
            print(f"Lives remaining: {lives}")

        else:
            print("Invalid input, only letters are accepted")


def main():
    print(hangman_title)
    print("Welcome to Hangman! Guess all the letters and reveal the word!\n")
    #word = get_word()
    show_status(word)
    play()


main()
