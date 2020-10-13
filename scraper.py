import requests 
from bs4 import BeautifulSoup
import smtplib
import time


class TrackPrice:
    
    def __init__(self):
        self.url="https://www.amazon.com/Acer-Predator-i7-9750H-Keyboard-PH315-52-78VL/dp/B07QXLFLXT/ref=sr_1_6?dchild=1&keywords=helios+300&qid=1602549601&sr=8-6"

        self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
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