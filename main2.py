import schedule,os, smtplib 
import time 
import json,requests
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages
from bs4 import BeautifulSoup
from replit import db

# Load email credentials from environment variables
password=os.environ['mailPassword']
username=os.environ['mailUsername']


def sendMail():
 
  email = db["Price"]
  server = "smtp.gmail.com" # Address of the mail server, change it to yours if you need to
  port = 587 # Port of the mail server, change it to yours if you need to
  s = smtplib.SMTP(host = server, port = port) # Creates the server connection using the host and port details
  s.starttls() # Sets the encryption mode
  s.login(username, password) # Logs into the email server for us

  msg = MIMEMultipart() # Creates the message
  msg['To'] = "chijn.kong.156@gmail.com" # Sets the receiver's email address
  msg['From'] = username # Sets the sender's email address
  msg['Subject'] = "PRICE STRIKE! TIME TO PURCHASE!"
  msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html

  s.send_message(msg) # Sends the message
  del msg # Deletes the message from memory

#Scrape product  pricing
def priceUpdate():
  url="https://www.alibaba.com/product-detail/Wholesale-for-Cheap-Original-Used-Version_1600991881518.html?spm=a2700.galleryofferlist.wending_right.9.1ddce89aLxkkf6"

  data=requests.get(url)
  soup=BeautifulSoup(data.text,"html.parser")


 
  for price_div in soup.find_all("div", {"class":"layout-body"}):
    
    price_current=price_div.find("div",{"class":"price"})
    for int in  price_current:
      price_current=int.text
        
          
    
    
  db["Price"]={"Current Price":price_current,"Desired Price":"$49.99", "Last Checked":time.ctime(),"PURCHASE URL":url}
    
#A schedule function that will send an email to the email address everyday at a specific time
priceUpdate()
schedule.every().day.at("00:00").do(priceUpdate)
while True:
  schedule.run_pending()
  time.sleep(1)


for price in db:
  if db["Current Price"] < db["desired_price"]:
    sendMail()
