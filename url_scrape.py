from bs4 import BeautifulSoup, SoupStrainer
import requests

with open('campinglist.html') as html_file:
	soup = BeautifulSoup(html_file, features="html.parser")

for match in soup.find_all('div', class_='flex-col-12'):
	headline = match.div.a
	path = (headline['href'])
	campcode = path[-6:]
	f=open("parkscan.txt", "a+")
	f.write("%s \n" % campcode)
	
	# print(match.prettify())
# for link in soup.find_all('a'):
#     print(link.get('href'))

# links = soup.find_all('a')

# for link in links:
#     print(link)
# match = soup.ATTRIBUTE.text
# print(match)