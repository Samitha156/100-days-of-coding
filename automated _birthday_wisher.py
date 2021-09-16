import pandas
import datetime as dt
import random
import smtplib

my_email = "sami.smtptest@gmail.com"
password = "0757230067"


def select_wish(index):
    index_num = index
    wish_list = []
    with open("letter_1.txt") as letter_1:
        first_wish = letter_1.readlines()
        wish_list.append(first_wish)
    with open("letter_2.txt") as letter_2:
        second_wish = letter_2.readlines()
        wish_list.append(second_wish)
    wish = random.choice(wish_list)
    send_wish(wish, index_num)


def send_wish(wish, index):
    receiver = f"Hey {birthdays.at[index, 'name']} "
    email = f"{birthdays.at[index, 'email']}"
    wish[0] = receiver
    birthday_wish = ''.join(wish)
    print(f"Email sent to {receiver} at {email}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!! \n\n {birthday_wish}"
        )


birthdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
date = now.date()

try:
    for i in range(len(birthdays["name"])):
        if date.month == birthdays.at[i, 'month'] and date.day == birthdays.at[i, 'day']:
            select_wish(i)
except:
    print("No birthdays!")
