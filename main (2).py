# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
lower_name1 = name1.lower()
lower_name2 = name2.lower()
names_together = lower_name1 + lower_name2
#print(names_together)
True_T = names_together.count("t")
True_R = names_together.count("r")
True_U = names_together.count("U")
True_E = names_together.count("e")

total_in_true = True_T + True_R + True_U + True_E

Love_L = names_together.count("l")
Love_O = names_together.count("o")
Love_v = names_together.count("v")
Love_e = names_together.count("e")

total_in_love = Love_L + Love_O + Love_v + Love_e

final_result = int(f"{total_in_true}{total_in_love}")

print(final_result)

#Write your code below this line 👇


