import random
import hangman_list
import hangman_stages

chosen_word = random.choice(hangman_list.word_list)
lenght_word = len(chosen_word)

lives = 6

# Empty list called "display" for each letter in the word

display = []

for _ in range(lenght_word):
    display.extend("_")

#print(display)


# Loop through each position in the chosen_word;

def replace_letter():
    for position in range(lenght_word):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
      


end_of_game = False

# While loop

while not end_of_game:
    guess = input("\n Put a letter here: ").lower()
    replace_letter()

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("\n You lose!")

        if lives > 0:
            print(hangman_stages.stages[lives+1])
            print(f"You guessed {guess}, that letter is not in the word. You lose a life, try again!")


    print(f"\n {' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\n You win!")
