#dependencies
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlencode

 
#list of URLs
urls = [
    'https://finance.yahoo.com/quote/TTM?p=TTM&.tsrc=fin-srch',
    'https://finance.yahoo.com/quote/F?p=F',
]
 
#starting our CSV file
file = open('stockprices.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Company', 'Price', 'Change'])
 
#looping through our list
for url in urls:
 
    #sending our request through ScraperAPI
    #params = {'api_key': 'b3f6880e570465aa875691b9bc8d420e', 'url': url}
    #page = requests.get('http://scraperapi.com/', params=urlencode(params))
    page=requests.get(url)
    #our parser
    soup = BeautifulSoup(page.text, 'html.parser')
    company = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    change = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).find_all('span')[2].text
 
    #printing to have some visual feedback
    print('Loading :', url)
    print(company, price, change)
 
#writing the data into our CSV file
writer.writerow([company.encode('utf-8'), price.encode('utf-8'), change.encode('utf-8')])
 
file.close()