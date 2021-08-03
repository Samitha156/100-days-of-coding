# from art import logo, vs
# from game_data import data
# import random
# from replit import clear

# def format_data(account):
#   """Takes the account data and returns the printable format."""
#   account_name = account["name"]
#   account_descr = account["description"]
#   account_country = account["country"]
#   return f"{account_name}, a {account_descr}, from {account_country}"

# def check_answer(guess, a_followers, b_followers):
#   """Take the user guess and follower counts and returns if they got it right."""
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"

# # Display art
# print(logo)
# score = 0
# game_should_continue = True
# # Generate a random account from the game data.
# account_b = random.choice(data)

# # Make the game repeatable.
# while game_should_continue:

#   # Making account at position B become the next account at position A.
#   account_a = account_b
#   account_b = random.choice(data)

#   if account_a == account_b:
#     account_b = random.choice(data)

#   print(f"Compare A: {format_data(account_a)}.")
#   print(vs)
#   print(f"Against B: {format_data(account_b)}.")

#   # Ask user for a guess.
#   guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#   # Check if user is correct.
#   ## Get follower count of each account.
#   a_follower_count = account_a["follower_count"]
#   b_follower_count = account_b["follower_count"]
#   is_correct = check_answer(guess, a_follower_count, b_follower_count)

#   # Clear the screen between rounds.
#   clear()
#   print(logo)
  
#   # Give user feedback on their guess.
#   # Score keeping.
#   if is_correct:
#     score += 1
#     print(f"You're right! Current score: {score}.")
#   else:
#     game_should_continue = False
#     print(f"Sorry, that's wrong. Final score: {score}.")

import random
from art import logo,vs
from game_data import data
from replit import clear

def format_data(account):
  """take the account data and returns the printable format"""
  account_name = account["name"]
  account_descrp = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descrp}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
  """Takes the user guess and details of follower count and returns if they got it right"""
  if a_follower_count > b_follower_count:
    return guess == "a"
  else:
    return guess == "b"



score = 0
game_continue = True
account_a = random.choice(data)

while game_continue:
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(logo)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  #Ask user for guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()


  #take the follower account
  a_followers_count = account_a["follower_count"]
  b_followers_count =  account_b["follower_count"]
  #check if user is correct
  is_correct = check_answer(guess, a_followers_count, b_followers_count)

  clear()

  if is_correct:
    score += 1
    print(f"you are right , your score is: {score}.")
  else:
    game_continue = False
    print(f"That's wrong, your score is: {score}")
  account_a = account_b
# def person_generator(data, letter):
#   data_select = random.choice(data)
#   name = data_select["name"]
#   occupation = data_select["description"]
#   country = data_select["country"]
#   celeb_info = (f"Compare {letter}: {name} , {occupation},from {country}")
#   return (celeb_info, data_select)

# def comparison(first_insta, second_insta, user_input):
#   winner = ""
#   user_score = 0
#   if int(first_insta) > int(second_insta):
#     winner = "A"
#   else:
#     winner = "B"
#   if user_score >= 0:  
#     if user_input == winner:
#       user_score += 1
#       print("you are correct!")
#     else:
#       print("you wrong")
#       user_score -= 1
#     print(f"{user_score}")
#   else:
#     print("Game over")
#     clear()
#   return winner



# print(logo)
# first_person,  first_dict = person_generator(data , "A")
# print(first_person)
# print(vs)
# second_person, second_dict = person_generator(data, "B")
# print(second_person)
# user_input =  input("who has more followers: Type 'A' or 'B' : ")
# check_answer = comparison(first_person,second_person, user_input)


# if check_answer == "A":
#   new_name = first_person
# else:
#   new_name = second_person





  