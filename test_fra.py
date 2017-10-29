
# Testing webscraping with beautifulsoup
# link to tutorial: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe


# import libraries
# import urllib2 # not working under python3.5 ?
import requests
from bs4 import BeautifulSoup

# specify the url
# quote_page = 'http://pubblicita.tribunale.milano.it/aste/cerca?provincia=MI&comune=F205&cap=&indirizzo=&tipologia=0&tipologia_dettaglio=0&limit=10&orderby=&prezzo_da=&prezzo_a=&data_vendita=&tipo_procedura=0&rge=&rge_anno=&enti_esattoriali=&quota=&tipologia_lotto=immobiliare'

# limiting 1000
quote_page = 'http://pubblicita.tribunale.milano.it/aste/cerca?provincia=MI&comune=F205&cap=&indirizzo=&tipologia=0&tipologia_dettaglio=0&limit=1000&orderby=&prezzo_da=&prezzo_a=&data_vendita=&tipo_procedura=0&rge=&rge_anno=&enti_esattoriali=&quota=&tipologia_lotto=immobiliare'

# query the website and return the html to the variable
page = requests.get(quote_page)
print(page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify()) # used only for analysing parsed page

# extract one information - indirizzo
# price_box = soup.find('div', attrs={'text-justify'})
# price = price_box.text
# print(price)

# find all information indirizzi (text-justify)
all_indirizzi = soup.find_all(class_="text-justify")
indirizzo = all_indirizzi[0].text
print(indirizzo)

# find all prices (col-xs-6 text-center)
all_prices = soup.find_all(class_="col-xs-6 text-center margin-bottom")
prezzo = all_prices[0].text
print(prezzo)

# create dataset with all indirizi
data = []
len_all_info = len(all_indirizzi)
for idx in range(len_all_info):
    parsed_text = all_indirizzi[idx].text
    data.append(parsed_text)
    print(parsed_text)

# csv exp
import csv
from datetime import datetime

with open('test_fra_exp.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(data)

# testing with pandas
# import pandas
# df = pandas.DataFrame(data={"col1": list_1})
# df.to_csv("./file.csv", sep=',',index=False)

