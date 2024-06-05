import random
from hangman_art import logo
from hangman_words import word_list 
#from replit import clear

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

end_of_game = False
## Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #clear()
    
    if guess in display:
        print(f"You've already guessed {guess}\n")
    
#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose...")

    print(f"{' '.join(display)}")
    
#Check if user has got all letters.
    if "_" not in display and " " not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])
    
  #this will show a solutination  
print(f'damn the soltion is: {chosen_word}.')
    
