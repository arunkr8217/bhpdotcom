import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def random_string(length=10):
    letter=string.ascii_letters
    return "".join(random.choice(letter) for i in range(length))
def link_sending(email,name,link):
    msg=MIMEMultipart()
    msg["From"]="bhptale"
    msg["To"]=email
    msg["Subject"]="verification_link"
    body="Hello, "+name+"your verification link "+link
    msg.attach(MIMEText(body,"plain"))
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("bhptale@gmail.com","Arun123..")
    text=msg.as_string()
    server.sendmail("bhptale@gmail.com",email,text)
    server.quit()

