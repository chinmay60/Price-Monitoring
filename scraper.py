import requests 
from bs4 import BeautifulSoup

url="https://www.amazon.com/Acer-Predator-i7-9750H-Keyboard-PH315-52-78VL/dp/B07QXLFLXT/ref=sr_1_6?dchild=1&keywords=helios+300&qid=1602549601&sr=8-6"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[1:6].replace(',',''))

if(converted_price < 1000):
    
print(converted_price)