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


continue_calculation = True
first_round_done = False

while continue_calculation:
  if not first_round_done:
    first_number = int(input("Enter your first number: "))
    select_operator =  input("Enter the operator as + - / * : ")
    second_number =  int(input("Enter your second number: "))

  final_value = calculator(first_number, second_number, select_operator )
  print(f"{first_number} {select_operator} {second_number} = {final_value}")

  should_continue = input("Enter another number? : type 'y' or 'n'").lower()
  if should_continue == "n":
    continue_calculation = False
  else:
    first_round_done = True
    first_number = final_value 
    second_number = int(input("Enter new number? : "))
    select_operator = input("Select operator + - * / : ")


