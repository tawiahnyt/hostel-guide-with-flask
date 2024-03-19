import smtplib

my_email = "tawiahnyt@gmail.com"
password = "qrtoyzgvmgrpwoza"

connection = smtplib.SMTP("SMTP.gmail.com")
connection.starttls()
connection.login(my_email, password)
connection.sendmail(from_addr=my_email,
                    to_addrs="tawiahnyt@gmail.com",
                    msg="Subject:New Registration Alert!!!\n\n {new_user.name} has just registered with email {new_user.email}.")
connection.close()