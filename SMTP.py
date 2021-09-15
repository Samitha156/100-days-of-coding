import smtplib
import datetime as dt
import random
import pandas

my_email = "sami.smtptest@gmail.com"
password = "0757230067"

time_now = dt.datetime.now()
weekday = time_now.weekday()
# data = pandas.read_txt("quotess.txt")
# print(data)
q_list = []
if weekday == 1:
    with open("quotess.txt") as all_quotes:
        quote = all_quotes.readlines()
        new_quote = random.choice(quote)
    print(new_quote)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="forloop.pub@yahoo.com",
            msg=f"Subject:Quote of the day \n\n {new_quote}"
        )

