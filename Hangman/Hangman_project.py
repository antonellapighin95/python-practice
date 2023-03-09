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


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Empty list called "display"

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
    
while not end_of_game:
    guess = input("\n Put a letter here: ").lower()
    replace_letter()
    #print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\n You lose!")
        if lives > 0:
            print(stages[lives+1])


    print(f"\n {' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\n You win!")
