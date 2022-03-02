import smtplib,ssl,getpass,requests,datetime           #smtplib defines an SMTP, ssl for secure connection
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



now=datetime.datetime.now()
content=''
def extract_weather(url):
    print("Extracting weather\n")
    info=''
    responce=requests.get(url)                           #get the whole html code
    soup=BeautifulSoup(responce.content,'html.parser')   #organize the html code
    temp=soup.find("div", attrs={"class": "h2"}).text    #extract temperature from the html code
    sky=soup.find("p").text                              #extract sky situation
    info="City: "+city+" | Temperature: "+temp+" | Sky: "+sky+"\n"
    return info

sender_email=""
receiver_email=""
password=getpass.getpass(prompt="Enter your password: ")
city=input("Enter city")
url="https://www.timeanddate.com/weather/india/"+city
content=extract_weather(url)




message=MIMEMultipart()     #MIMEMultipart is used when we have attachments or want to provide alternative versions of the same content (e.g. a plain text/HTML version)
message["Subject"]="Weather today! "+"Dated: "+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
message["From"]=sender_email
message["To"]=receiver_email
message.attach(MIMEText(content,'html'))



context=ssl.create_default_context()   #A necessary security measure- Ensures secure default settings
smtp_server="smtp.gmail.com"           #for establishing a secure connection to the GMAIL server
port=587
server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context)
server.login(sender_email,password)
print("successful\n")


server.sendmail(sender_email,receiver_email,message.as_string())
