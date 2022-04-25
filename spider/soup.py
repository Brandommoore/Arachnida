import sys
import urllib.request
from cgitb import html
from bs4 import BeautifulSoup

def img_routes(url):
	# url request
	datos = urllib.request.urlopen(url).read().decode()
	# soup
	soup = BeautifulSoup(datos, "html.parser")
	# creating a tag
	tags = soup('img')
	for tag in tags:
		print(tag.get('src'))
		print("\n")
	print("\n")

url = sys.argv[1]
print(url)

img_routes(url)

# find img with find
#print(soup.find_all("a", limit=1))
#print("\n")

# tit = soup.title
#print(soup.title)
# print(soup.prettify())