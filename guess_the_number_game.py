from random import randint
from art import logo
from replit import clear

EASY_LEVEL_STEP = 10
HARD_LEVEL_STEP = 5

def generate_number():
  select_number = randint(1,100)
  return select_number

def set_difficulty():
  game_level = input("choose difficulty level Type 'easy' or 'hard':")
  if game_level == "hard":
    return HARD_LEVEL_STEP
  else:
    return EASY_LEVEL_STEP



def game(number, level):
  exit_game = False
  while level > 0 and not exit_game:
    level -= 1
    user_guess = int(input("make a guess : "))
    if user_guess == number:
      print("you win!")
      exit_game = True
    elif user_guess > number:
      print(f"Too high! guess again \nyou have {level} number of attempts")
    elif user_guess < number:
      print(f"Too_low! guess again \nyou have {level} number of attempts")

def generator():
  clear()
  print(logo)
  print("welcome to the guessing game")
  computer_number = generate_number()
  turns = set_difficulty()
  print(f"you have {turns} attempts to guess the number")
  print("I'm thinking a number")
  game(computer_number, turns)

should_continue = True
while should_continue: 
  user_decision = input("Do you want to play? Type 'y' or 'n': ")
  if user_decision == "y":
    generator()
  else:
    should_continue = False
    clear()

