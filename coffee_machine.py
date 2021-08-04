MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def beverage_price(beverage):
  beverage_details = MENU[beverage]
  beverage_cost = beverage_details["cost"]
  return beverage_cost

def money_calculator(q, d, n ,p, cost):
  total_in = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
  if cost < total_in:
    return round(total_in - cost, 2)

def resource_updater(resources, beverage):
  updated_resources = {}
  beverage_details = MENU[beverage]
  updated_resources["water"] = int(resources["water"]) - int(beverage_details["ingredients"]["water"])
  updated_resources["milk"] = int(resources["milk"])- int(beverage_details["ingredients"]["milk"])
  updated_resources["coffee"] = int(resources["coffee"]) - int(beverage_details["ingredients"]["coffee"])
  return updated_resources

def resource_checker(resources, beverage):
  beverage_details = MENU[beverage]
  check_water = int(resources["water"]) - int(beverage_details["ingredients"]["water"])
  check_milk = int(resources["milk"]) - int(beverage_details["ingredients"]["milk"])
  check_coffee = int(resources["coffee"]) - int(beverage_details["ingredients"]["coffee"])
  if check_water > 0 and check_milk > 0 and check_coffee > 0 :
    return True



profit = 0
resources = {
  "water":300, 
  "milk" : 200, 
  "coffee": 100,
}


#Take user input about what they like
#whenever they ask report then print the current report
user_request = True
while user_request:
  user_request = input("What would you like? (espresso/latte/cappuccino):")
  if user_request == "report":
    print(f"water : {resources['water']}ml")
    print(f"milk : {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}g")
    print(f"money : {profit}$")

  else:
    if resource_checker(resources, user_request):
      bill_cost = beverage_price(user_request)
      print("Please insert coins")
      num_quaters = int(input("how many quaters? :"))
      num_dimes = int(input("how many dimes? :"))
      num_nickles = int(input("how many nickles? :"))
      num_pennies = int(input("how many pennies? :"))
      balance = money_calculator(num_quaters, num_dimes,num_nickles, num_pennies, bill_cost)
      profit += bill_cost
      if balance:
        print(f"Here is ${balance} in change")
        print(f"Here is your {user_request}")
      else:
        print("sorry that's not enough money. Money refunded!")
      # print(resource_updater(resources, user_request))
      resources = resource_updater(resources, user_request)
    else:
      print("some resource is not enough!")
  



#Ask to insert coin with each coin value


#calculate the total coins value


#if the payment is enough then give the beverage and balance

#update the report
