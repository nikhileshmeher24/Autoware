import requests
from bs4 import BeautifulSoup
import smtplib,ssl,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

from requests_toolbelt import MultipartEncoder
now=datetime.datetime.now()

content=''
def extract_news(url):
    print("Extracting IndianExpress Stories\n")
    info=''
    info+=('<b>IndianExpress Stories</b>\n'+'<br>')
    responce=requests.get("https://indianexpress.com/section/cities/bangalore/")
    soup=BeautifulSoup(responce.content,'html.parser')
    headlines=soup.find_all('h3')

    for i in range(len(headlines)):
        info+=((str(i+1)+'::'+headlines[i].text+"\n"+'<br>'))

    return (info)

cnt=extract_news('https://indianexpress.com/section/cities/bangalore/')
content+=cnt
content+=('<br>-------<br>')
content+=('End of message')


smtp_server="smtp.gmail.com"
port=587
sender_email=""
receiver_email=""

message=MIMEMultipart()
message["Subject"]="News Headline Emailer "+"Dated: "+str(now.day)
message["From"]=sender_email
message["To"]=receiver_email
message.attach(MIMEText(content,'html'))

password=""
context=ssl.create_default_context()
server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context)
server.login(sender_email,password)
print("successful\n")

server.sendmail(sender_email,receiver_email,message.as_string())

