# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
initial_check01 = year / 4
initial_check02 = year / 100
initial_check03 = year / 400
if (initial_check01 % 2 == 0):
    if (initial_check02 % 2 == 0):
        if (initial_check03 % 2 == 0):
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("Not a leap year")

#Write your code below this line 👇
