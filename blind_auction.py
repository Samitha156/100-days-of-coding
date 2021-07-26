from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid_dict = {}
finish_bidding = False

def find_highest_bidder(bidding_record):
  start_bid = 0 
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > start_bid:
      winner = bidder
      max_bid = bidding_record[bidder]
      start_bid = bidding_record[bidder]
  print(f"The winner is {winner} with bid of ${max_bid}")


while not finish_bidding:
  name =  input("Enter your name:")
  price =  int(input("Enter bid amount: $"))
  bid_dict[name] =  price
  should_continue = input("is there any players? Type 'yes' or 'no' :").lower()
  if should_continue == "no":
    finish_bidding = True
    find_highest_bidder(bid_dict)
  elif should_continue == "yes":
    clear()
  

