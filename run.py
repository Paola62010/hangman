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
word = "area"
hidden = (len(word) * "_")


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
    print(hidden)


def play():
    global guessed, missed, lives, game_complete, hidden
    while game_complete is False and lives > 0:
        guess = input("Guess a letter or the entire word: \n").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in word and not len(guessed) == len(word) - 1:
                occurences = findOccurrences(word, guess)
                for index in occurences:
                    hidden = hidden[:index] + guess + hidden[index + 1:]
                show_status(word)
                print(f"Well done, '{guess}' is part of the word!")
                guessed.append(occurences)
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print(guessed)
            elif guess in word and len(guessed) == len(word) - 1:
                show_status(word)
                print(f"Congratulations, the correct word was '{word}'!")
                game_complete = True
            elif guess not in word and lives != 1:
                show_status(word)
                print(f"Sorry, '{guess}' is not part of the word. Try again.")
                missed.append(guess)
                lives -= 1
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
            else:
                show_status(word)
                print(f"Sorry, the correct word was '{word}'...")
                game_complete = True
        elif guess == word and guess.isalpha():
            if guess == word:
                show_status(word)
                print("Congratulations, the correct word was '{word}'!")
                game_complete = True
        elif guess != word and guess.isalpha():
            show_status(word)
            print(f"Sorry, {guess} is not the correct word")
            lives -= 1
            print(f"Lives remaining: {lives}")

        else:
            show_status(word)
            print("Invalid input, only letters are accepted")


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def main():
    print(hangman_title)
    print("Welcome to Hangman! Guess all the letters and reveal the word!\n")
    #word = get_word()
    show_status(word)
    play()


main()
