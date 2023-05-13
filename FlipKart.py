import requests
from bs4 import BeautifulSoup
import pandas as pd

flipkart = []
for i in range(100):
    url = f"https://www.flipkart.com/search?q=mobiles+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show" \
          f"=on&as=off&page={i} "
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    phones = soup.find_all('div', '_3pLy-c row')
    for phone in phones:
        d = {}
        name = phone.find('div', '_4rR01T').get_text()
        price = soup.find('div', '_30jeq3 _1_WHN1').get_text()
        rating = soup.find('div', '_3LWZlK').get_text()
        d['Brand_name'] = name.split(' ')[0]
        d['Phone_name'] = name
        d['Price'] = price
        d['Rating'] = rating
        flipkart.append(d)

mydata = pd.json_normalize(flipkart)
mydata.to_excel('FliplartPhones.xlsx')

