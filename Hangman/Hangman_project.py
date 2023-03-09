import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Empty list called "display"

display = []

for _ in range(lenght_word):
    display.extend("_")

print(display)


# Loop through each position in the chosen_word;

def replace_letter():
    for position in range(lenght_word):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

def are_dashes():
    return "_" in display
    # for l in display:
    #     if l == "_":
    #         return True
    # return False
    
while are_dashes():
    guess = input("Guess a letter: ").lower()
    replace_letter()
    print(display)

if "_" not in display:
    print("You win!")