
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word=random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

print(chosen_word)

guess_count=0

guess_word=[]

lives=6
wrong_guess_count=0
intermediate_guess_count=0

for i in range(0,len(chosen_word)):
    guess_word.append("_")

print(stages[0])

while lives != 0:
    print(guess_word)
    guess = input("Guess and enter a letter: ").lower()
    intermediate_guess_count=guess_count
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            guess_count += 1
            guess_word[i] = guess
    if intermediate_guess_count == guess_count:
        wrong_guess_count += 1
        print(stages[wrong_guess_count])
        lives -= 1
        print(lives)
        if lives == 0:
            print("You hv lost")
            break
    if "_" not in guess_word:
        print("You Won")
        break

