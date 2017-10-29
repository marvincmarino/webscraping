
# Testing webscraping with beautifulsoup
# link to tutorial: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe


# import libraries
# import urllib2 # not working under python3.5 ?
import requests
from bs4 import BeautifulSoup

# get price

# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable
page = requests.get(quote_page)
page

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text
print(price)

# export to csv

import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])

