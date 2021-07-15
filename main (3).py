import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
seed = int(input("enter seed number:"))

number_of_members = len(names)

random_number = random.randint(0, number_of_members)
print("The bill should be paid by "+ names[random_number])

