import random
from hangman_word_list import word_list
from hangman_art import stages, logo

print(logo)
#chosen_word is the word chosen by the code
chosen_word = random.choice(word_list)

#blank is the current state of blanks
blank = ""

#word_length is the length of the word
word_length = len(chosen_word)

#correct_letters is the list of correct letters guessed by the user
correct_letters = []
wrong_letters = []

for a in range(0, word_length):
    blank = " _" + blank
    correct_letters.append(" _")

print(blank)
display = ""

lives = 6

while display != chosen_word and lives != 0:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    #guess is the guess by the user
    guess = input("Guess a letter: ").lower()


    if (guess not in chosen_word) and (guess not in wrong_letters):
        lives -= 1
        wrong_letters.append(guess)
    elif guess in wrong_letters:
        print(f"You have already guessed '{guess}' and its not in the word.")

    if guess in correct_letters:
        print(f"You have already guessed '{guess}' and it is in the word.")

    a = 0
    for letter in chosen_word:
        if letter == guess:
            correct_letters[a] = guess
        a += 1

    display = ""

    for a in range(word_length):
        display += correct_letters[a]

    #display is the final output after a single guess
    print(display + "\n\n\n\n")
    print(stages[(-1 * (lives+1))])

    if "_" not in display:
        print("****************************YOU WIN****************************")
    
    elif lives == 0:
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    print(lives)