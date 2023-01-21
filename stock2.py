from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from csv import writer
import csv
from urllib.parse import urlencode


s=HTMLSession()
City=input("enter stock name : ")
query=City
url = f'https://finance.yahoo.com/quote/{query}?p={query}&.tsrc=fin-srch'
r=s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
soup=BeautifulSoup(r.text, 'html.parser')
#print(soup)
company = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
price_Atclose=soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

price_PreMarket=soup.find('fin-streamer', {'class':'C($primaryColor) Fz(24px) Fw(b)'}).text
print('Price at close:'+ price_Atclose,' and ','Price pre-market:'+ price_PreMarket)

file = open('stockprices2.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Company', 'Priceprice_Atclose', 'price_PreMarket'])

writer.writerow([company.encode('utf-8'), price_Atclose.encode('utf-8'), price_PreMarket.encode('utf-8')])

        
