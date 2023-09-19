import random;

from hangman_art import stages,logo
from hangman_words import word_list


words = ['ardvark', 'camel','dog']
random_word = random.choice(word_list)
lives = 6


print(logo)
print("The random word is " + random_word)

display = []

for dash in range(len(random_word)):
    display += "_"
    
print(display) 

end_game = False


while not end_game:
    guess = input("Guess a letter ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            end_game = True
                   
    if "_" not in display:
        print("You Win")
        end_game = True
    print(stages[lives])