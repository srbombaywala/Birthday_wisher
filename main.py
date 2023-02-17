##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random


my_email = "srbombaywala@gmail.com"
password = "12312323" # new app password from gmail setting after enabling 2 step verification


now = dt.datetime.now()
curr_month = dt.datetime.now().month
curr_date = dt.datetime.now().day


birthday_file = pandas.read_csv("birthdays.csv")
birthday = pandas.DataFrame(birthday_file)
curr_birthday = birthday[(birthday["month"]==curr_month) & (birthday["day"]==curr_date)] #dataframe consisting of all the birthdays in current month
curr_birthday.reset_index(inplace=True)


if len(curr_birthday)>0:
    for i in range(len(curr_birthday)):
        birthday_name = curr_birthday.loc[i,"name"]

        letter = random.randint(1,3)
        with open(f"letter_templates/letter_{letter}.txt") as birthday_letter:
            wish = birthday_letter.read()
            birthday_wish = wish.replace("[NAME]",birthday_name)

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=curr_birthday.loc[i,"email"],
                msg=f"Subject:Happy Birthday\n\n{birthday_wish}"
            )