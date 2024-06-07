import random

# List of words for the game
words = ["apple", "banana", "orange", "computer", "python", "programming"]

# Visual representation of hangman stages
stages = [  # final index is life lost
            """
              --------
             |      |
             |      
             |      
             |      
             |      
            |________
    """,
            """
              --------
             |      |
             |      O
             |      
             |      
             |      
            |________
    """,
            """
              --------
             |      |
             |      O
             |      |
             |      
             |      
            |________
    """,
            """
              --------
             |      |
             |      O
             |     /|\
             |      
             |      
            |________
    """,
            """
              --------
             |      |
             |      O
             |     /|\
             |     / 
             |      
            |________
    """,
            """
              --------
             |      |
             |      O
             |     /|\
             |     / \
             |      
            |________
    """
]

def get_word():
  """Chooses a random word from the list"""
  word = random.choice(words)
  return word

def display_hangman(lives):
  """Prints the visual representation based on lives remaining"""
  print(stages[lives])

def display_progress(word, guessed):
  """Displays the word progress with underscores and guessed letters"""
  progress = ["_" for _ in word]
  for i in range(len(word)):
    if word[i] in guessed:
      progress[i] = word[i]
  print(" ".join(progress))

def get_guess():
  """Gets a guess from the player and validates it"""
  while True:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid guess. Please enter a single letter.")
    else:
      return guess

def play(word, lives):
  """Main game loop"""
  guessed = set()
  while lives > 0:
    # Display progress
    display_hangman(lives)
    display_progress(word, guessed)

    # Get guess
    guess = get_guess()
    
    # Check guess
    if guess in word:
      guessed.add(guess)
    else:
      lives -= 1
      print(f"Incorrect guess. You have {lives} lives remaining.")

    # Check win or lose
    if all(letter in guessed for letter in word):
      print(f"You win! The word was {word}.")
      break
  
  if lives == 0:
    display_hangman(lives)
    print(f"You lose. The word was {word}.")

def main():
  """Starts the game"""
  word = get_word()
  lives = len(stages) - 1
  play(word, lives)

  # Option to play again
  while True:
    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
      main()
      break
    elif play_again == 'n':
      print("Thanks for playing!")
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
  main()
