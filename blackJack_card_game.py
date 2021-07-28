############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from replit import clear
from art import logo
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score of cards"""
  if sum(cards) == 21 and len(cards) ==2:  
    return 0


#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose , opponent has blackjack"
  elif user_score == 0:
    return "win with a blackjack"
  elif user_score > 21:
    return "you went over. Lose!"
  elif computer_score > 21:
    return "opponent went over. You win"
  elif user_score > computer_score:
    return "you wins"
  else:
    return "you lose"


def play_game():

  print(logo)
  user_cards = []
  computer_cards = []


  for number in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_gameover = False
  while not is_gameover:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards}, current score : {user_score}")
    print(f"Computer's first card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score >21:
      is_gameover = True
    else:
      user_should_deal = input("Type 'D' to deal or 'N' to pass: ").lower()
      if user_should_deal == "d":
        user_cards.append(deal_card())
      else:
        is_gameover = True

  #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    # print(f"computer's cards {computer_cards}, current score is : {computer_score}")
  print(f"computers final hand is {computer_cards}and score is {computer_score}")
  print(compare(user_score, computer_score))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("wanna play blackjack game? 'y' or n : ") == "y":
  clear()
  play_game()


# import random


# def deal_card(cards):
#   generated_card = []

#   gen_card = random.choice(cards)
#   generated_card.append(gen_card)
#   return generated_card

# def calculate_cards(card_list):
#   sum_cards = 0
#   for card in card_list:
#     sum_cards += card
#   return sum_cards

# def compare_scores(user_score , computer_score):
#   if user_score > computer_score:
#     return "user_wins"
#   else: 
#     return "compurer_wins"

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_start_Cards = random.sample(cards, 2)
# start_sum =  calculate_cards(player_start_Cards)
# print(f"{player_start_Cards} your sum is : {start_sum}")
# computer_start_cards =  random.sample(cards, 2)
# computer_start_sum = calculate_cards(computer_start_cards)
# print(computer_start_cards)

# should_continue = True

# while should_continue:
#   user_continue = input("Deal or Hold? type 'D' or 'H': ").lower()
#   if user_continue == "d":
#     new_card = deal_card(cards)
#     new_start_Cards = player_start_Cards
#     new_start_Cards +=  new_card
#     new_sum_user = calculate_cards(new_start_Cards)
#     print(f"{new_start_Cards} new sum is : {new_sum_user}")
#     if new_sum_user > 20:
#       print(f"computer cards are : {computer_start_cards} sum is {computer_start_sum} \n You Lose!")
#       should_continue = False
#   elif user_continue == "h":





