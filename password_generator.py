# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for char in range(1, nr_letters+1):
#   random_letter = random.choice(letters)
#   password += random_letter
# for symb in range(1, nr_symbols+1):
#   random_symb = random.choice(symbols)
#   password += random_symb
# for num in range(1, nr_numbers+1):
#   random_num = random.choice(numbers)
#   password += random_num

# print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for symb in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

hard_password = ""
for character in password_list:
    hard_password += character
print(hard_password)

# total_len =  nr_letters + nr_numbers + nr_symbols

# hard_password = ""
# for letter in range(1, total_len + 1):
#   random_char = random.choice(password_list)
#   hard_password += random_char
# print(hard_password)

trave_log= {
    "France": {"cities_visited":["paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["berlin", "hamburg", "Statu"], "total_visits": 12}
}