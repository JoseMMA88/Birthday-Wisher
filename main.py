##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

my_email = "dimitryps3@hotmail.com"
password = "----------"


data_frame = pandas.read_csv("birthdays.csv")
print(data_frame)
dic = data_frame.to_dict(orient="records")

for birth in dic:
    if birth["month"] == dt.datetime.now().month and birth["day"] == dt.datetime.now().day:

        with smtplib.SMTP("smtp.live.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
            with open(f"letter_templates/{random.choice(letter_list)}") as file:
                msg = file.read()
                msg = msg.replace("[NAME]", birth["name"])
                connection.sendmail(from_addr=my_email,
                                    to_addrs=birth["email"],
                                    msg=f"Subject: Happy Birthday!\n\n{msg}")

            connection.close()




