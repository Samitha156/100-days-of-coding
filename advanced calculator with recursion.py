from art import logo

print(logo)

def calculator(first_number, second_number, select_operator):
  if select_operator == "+":
    return first_number + second_number
  elif select_operator == "-":
    return first_number - second_number
  elif select_operator == "*":
    return first_number * second_number
  else:
    return first_number / second_number



#using recursion
def calculation():
  continue_calculation = True
  first_round_done = False
  first_number = int(input("Enter your first number: "))

  while continue_calculation:
    select_operator =  input("Enter the operator as + - / * : ")
    second_number =  int(input("Enter your second number: "))

    final_value = calculator(first_number, second_number, select_operator )
    print(f"{first_number} {select_operator} {second_number} = {final_value}")

    should_continue = input("Enter another number? : type 'y' or 'n' for new start").lower()
    if should_continue == "n":
      continue_calculation = False
      calculation()
    else:
      first_number = final_value 

calculation()
