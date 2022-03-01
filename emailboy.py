import smtplib,ssl,getpass
smtp_server="smtp.gmail.com"
port=587
sender_email="nikhileshmeher2021@gmail.com"
receiver_email="nikhileshmeher24@gmail.com"
message="hey there, this is an automated message"
password=getpass.getpass(prompt="Enter your password: ")
context=ssl.create_default_context()
server=smtplib.SMTP(smtp_server,port)
server.starttls(context=context)
server.login(sender_email,password)
print("successful\n")

server.sendmail(sender_email,receiver_email,message)
