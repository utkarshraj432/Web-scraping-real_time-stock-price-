from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

s=HTMLSession()
City=input("enter stock name : ")
query=City
url = f'https://finance.yahoo.com/quote/{query}?p={query}&.tsrc=fin-srch'

def currentPrice():
    r=s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
    soup=BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    price_Atclose=soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    #price_PreMarket=soup.find('fin-streamer', {'class':'C($primaryColor) Fz(24px) Fw(b)'}).text
    return price_Atclose

while True:
    print("Current price is:"+ str(currentPrice()))

