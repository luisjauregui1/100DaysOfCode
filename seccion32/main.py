import smtplib
import config
import random
import datetime as dt

my_email = config.correo_g
password = config.correo_pass
email_h = config.correo_h

ruta_quotes = "C:\\Users\\Gustavo\\Documents\\codigo\\100DaysOfCode\\seccion32\\quotes.txt"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open(ruta_quotes) as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:MOnday Motivation\n\n{quote}")
        



