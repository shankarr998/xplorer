# Python code to illustrate Sending mail 
# to multiple users 
# from your Gmail account 
import smtplib,random

# list of email_id to send the mail 
li = ["998shankar@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("the.explorer.verify@gmail.com", "8884233310")
    message = "otp"
    s.sendmail("sender_email_id", dest, message)
    s.quit()

