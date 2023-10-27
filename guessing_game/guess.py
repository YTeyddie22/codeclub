import random;

EASY_LEVEL = 10;
HARD_LEVEL = 5;

#Check for correctness
def checker(guess, answer, turns):
  """ 
  Checks for correctness between the guessed number and actual answer and also the number of turns
  """
  if guess < answer:
    print("Too Low");
    return turns - 1;
  elif guess > answer:
    print("Too high");
    return turns - 1;
  else:
    print("You got the number! huzzah!!");
    
def chooseDifficulty():
  """
  Checks for the difficulty of the game
  """
  choice =  input("Choose a difficulty. Type 'easy' or 'hard': ");
  if choice == "easy":
    return EASY_LEVEL;
  else:
    return HARD_LEVEL;

def game():
  print("Welcome to the Number Guessing Game");
  print("I'm thinking of a number between 1 and 100.");
  random_number = random.randint(1, 100);
  turns = chooseDifficulty();
  guess = 0;
  
  while guess != random_number:
    #User to guess the number
    print(f"You have {turns} attempts remaining to guess the number.");
    guess = int(input("Make a guess: "));
    turns = checker(guess,random_number,turns);
    
    if turns == 0:
      print("You have run out of guesses")
      return;
    
game();




  
  


 