from operator import truediv
import sys
import urllib.request
from cgitb import html
from bs4 import BeautifulSoup

# - img_routes -- return: whole list of images
# - check_images -- returm: correct url list images
#

def imgRoutes(url):
	img_url=[]
	# url request
	datos = urllib.request.urlopen(url).read().decode()
	# soup
	soup = BeautifulSoup(datos, "html.parser")
	# creating a tag
	tags = soup('img')
	for tag in tags:
		img_url.append(tag.get('src'))
	return(img_url)

def checkImages(img_url):
	myImgs=[]
	suffix=((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
	for elem in img_url:
		if elem.endswith(suffix):
			myImgs.append(elem)
	return(myImgs)


url = sys.argv[1]
# img_routes(url)

imgChecked=checkImages(imgRoutes(url))
print(imgChecked)

# imgsRout=img_routes(url)
# imgsRout.append("patata/roja.svg")
# print(imgsRout[:])
# print(checkImages(imgsRout))

# elem="siper/siiip/img.png"
# suffix=((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
# print(elem.endswith(suffix))

#img_routes(url)

# find img with find
#print(soup.find_all("a", limit=1))
#print("\n")

# tit = soup.title
#print(soup.title)
# print(soup.prettify())