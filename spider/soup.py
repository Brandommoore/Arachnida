from operator import truediv
import sys
import time
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

def findUrls(url):
	myUrls=[]
	data=urllib.request.urlopen(url).read().decode()
	soup=BeautifulSoup(data, "html.parser")
	tags=soup('a')
	for tag in tags:
		myUrls.append(tag.get('href'))
	return(myUrls)

def recUrls(myUrls):
	allUrls=[]
	for url in myUrls:
		#print(url + "\n")
		#print("  -- ")
		#print(findUrls(url))
		allUrls.append(findUrls(url))
		time.sleep(0.1)
	return(allUrls)

# cleanUrlList - return: list without duplicates
# chech if url in cleanList already exist
def cleanUrlList(urlList):
	cleanList=[]
	for url in urlList:
		cleanList.append(url)
		 #if cleanList in
	return(cleanList)

url = sys.argv[1]
# img_routes(url)

# print(findUrls(url))
# print("\n")
recUrls(findUrls(url))

#print(checkImages(imgRoutes(url)))

# imgChecked=checkImages(imgRoutes(url))
#print(imgChecked)

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