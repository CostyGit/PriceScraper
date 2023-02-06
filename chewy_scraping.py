import smtplib
import datetime
import time
import subprocess
import sys
import ssl
import csv
#import os


def install_bs4():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])


try:
    from bs4 import BeautifulSoup
except:
    install_bs4()
    from bs4 import BeautifulSoup


def install_requests():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])


try:
    import requests
except:
    install_requests()
    import requests


def install_pandas():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])


try:
    import pandas
except:
    install_pandas()
    import pandas

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


URL = "https://www.chewy.com/prettylitter-cat-litter/dp/659654?nav-submit-button=&ref-query=pretty%20litter&ref=searchRedirect"

# got user-agent info for my laptop from https://httpbin.org/get
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(class_='styles_productName__vSdxx').get_text()


price = soup2.find(class_='kib-product-price').get_text()

title = title.strip()
price = price.strip()[1:]

print(title)
print(price)

# add timestamp
today = datetime.date.today()

print(today)

# Create csv file, add price, automate process to append more items to csv
header = ['Title', 'Price', 'Date']
data = [title, price, today]

# with open('ChewyScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
#   writer = csv.writer(f)
#  writer.writerow(header)
# writer.writerow(data)

with open('ChewyScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# check_price()
# while(True):
 #   check_price()
  #  time.sleep(86400)

# to display data without having to open excel file
df = pandas.read_csv(
    r'C:\Users\utente\Desktop\Learning\Portfolio\scraping\ChewyScraperDataset.csv')

print(df)
