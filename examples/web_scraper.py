
import requests
from bs4 import BeautifulSoup

"""
Author: Chris Marciniak
Example to scrape a web page, extract links to pdf files and download those files

"""


def download_file(url):
	filename = url[32:len(url)]
	res = requests.get(url)
	file = open( filename , 'wb')
	file.write( res.content )
	file.close()

url = "http://web.maga.gob.gt/precios-agricolas/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html)

links = soup.select("div.one_half ul li a")

for link in links:
	url = link.get("href")
	print("Downloading "+link.get("href"))
	download_file(url)