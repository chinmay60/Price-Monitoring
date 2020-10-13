import requests 
from bs4 import BeautifulSoup
import smtplib
import time
import configparser


#init config file 
try:
    config = configparser.ConfigParser()
    config.read('config.ini')

except:
    print("NO config file found! please make sure config file exists and the path is correct")


#init all the variables
try:
    URL = config.get('config', 'URL')
    UserAgent = config.get('config', 'UserAgent') 
    YOUR_EMAIL = config.get('config', 'YOUR_EMAIL') 
    YOUR_PASSWORD = config.get('config', 'EMAIL_PASSWORD') 
except:
    print("please add all the parameters in config file")

class TrackPrice:
    
    def __init__(self):
        self.url=URL
        self.headers = {"User-Agent": UserAgent}
        self.title = ''



    def Check_Price(self):
        page = requests.get(self.url, headers=self.headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        self.title = soup.find(id="productTitle").get_text()
        price = soup.find(id="priceblock_ourprice").get_text()
        converted_price = float(price[1:6].replace(',',''))

        if(converted_price < 1000):
            self.send_mail()

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com')
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(YOUR_EMAIL, YOUR_PASSWORD)

        subject = 'Price for' + self.title + 'fell down!'

        body = 'Check the amazon link ' + self.url

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            YOUR_EMAIL,
            YOUR_EMAIL,
            msg
        )
        
        print('HEY EMAIL HAS BEEN SENT !')

        server.quit()

TrackPrice = TrackPrice()
while True:
    TrackPrice.Check_Price()
    time.sleep(60* 60 *24)