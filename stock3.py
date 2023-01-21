from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from csv import writer
import csv
from urllib.parse import urlencode


urls = [
    'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch',
    'https://finance.yahoo.com/quote/TTM?p=TTM&.tsrc=fin-srch',
    'https://finance.yahoo.com/quote/F?p=F',

]

file = open('stockprices3.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Company', 'price_Atclose', 'price_PreMarket'])

for url in urls:
    page=requests.get(url)
    #our parser
    soup = BeautifulSoup(page.text, 'html.parser')
    company = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    price_Atclose=soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    price_PreMarket=soup.find('fin-streamer', {'class':'C($primaryColor) Fz(24px) Fw(b)'}).text
    
    print(company,'Price at close:'+ price_Atclose,' and ','Price pre-market:'+ price_PreMarket)
    writer.writerow([company.encode('utf-8'), price_Atclose.encode('utf-8'), price_PreMarket.encode('utf-8')])

file.close()




        
