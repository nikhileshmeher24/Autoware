import smtplib,requests
from bs4 import BeautifulSoup
import smtplib,ssl,getpass
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


content=''
def extract_weather(url):
    print("Extracting weather\n")
    info=''
    responce=requests.get(url)
    soup=BeautifulSoup(responce.content,'html.parser')
    temp=soup.find("div", attrs={"class": "h2"}).text
    sky=soup.find("p").text
    info="City: "+city+" | Temperature: "+temp+" | Sky: "+sky+"\n"
    return info

now=datetime.datetime.now()
city=input("Enter city")
url="https://www.timeanddate.com/weather/india/"+city
cnt=extract_weather(url)
content+=cnt
content+=('<br>-------<br>')
content+=('End of message')
print(content)


smtp_server="smtp.gmail.com"
port=587
sender_email="nikhileshmeher2021@gmail.com"
receiver_email="nikhileshmeher24@gmail.com"
message=MIMEMultipart()
message["Subject"]="Weather today! "+"Dated: "+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
message["From"]=sender_email
message["To"]=receiver_email
message.attach(MIMEText(content,'html'))
password=getpass.getpass(prompt="Enter your password: ")
context=ssl.create_default_context()
server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context)
server.login(sender_email,password)
print("successful\n")


server.sendmail(sender_email,receiver_email,message.as_string())
