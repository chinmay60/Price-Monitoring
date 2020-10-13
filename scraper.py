import requests 
from bs4 import BeautifulSoup
import smtplib
import time


class TrackPrice:

    URL = '' #
    HEADERS = 'ENTER_USER_AGENT_INFO_HERE' #you can find this by simply Googling: what is my user agent
    YOUR_EMAIL = 'ENTER_YOUR_EMAIL_HERE' #'example@abc.com'
    

    def __init__(self):
        self.url=URL

        self.headers = {"User-Agent": HEADERS}
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

        server.login('ENTER_YOUR_EMAIL', 'ENTER YOUR PASSWORD')

        subject = 'Price for' + self.title + 'fell down!'

        body = 'Check the amazon link ' + self.url

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'ENTER_YOUR_EMAIL',
            'ENTER_YOUR_EMAIL',
            msg
        )
        
        print('HEY EMAIL HAS BEEN SENT')

        server.quit()

TrackPrice = TrackPrice()
while True:
    TrackPrice.Check_Price()
    time.sleep(60* 60 *24)