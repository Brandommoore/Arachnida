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
	try:
		datos = urllib.request.urlopen(url)
	except Exception as e:
		pass
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
	try:
		data=urllib.request.urlopen(url)
		soup=BeautifulSoup(data, "html.parser")
		tags=soup('a')
		for tag in tags:
			myUrls.append(tag.get('href'))
		# print(myUrls)
		return(myUrls)
	except Exception as e:
		return([])
		pass

def recUrls(myUrls):
	# print(myUrls)
	allUrls=[]
	for url in myUrls:
		#print(url + "\n")
		#print("  -- ")
		#print(findUrls(url))
		currentUrls=findUrls(url)
		allUrls.extend(currentUrls)
		time.sleep(0.1)
	print(allUrls)
	return(allUrls)

	# cleanUrlList - return: list without duplicates
	# chech if url in cleanList already exist
	# def cleanUrlList(urlList):
	# 	cleanList=[]
	# 	for url in urlList:
	# 		cleanList.append(url)

	# 	return(cleanList)

if __name__ == "__main__":

	url = sys.argv[1]
	# img_routes(url)
	allUrls=findUrls(url)
	recUrls(allUrls)

	# findUrls(url)

	# print(findUrls(url))
	# print("\n")
	# urls = recUrls(findUrls(url))
	# urls=findUrls(url)
	# finalUrls=recUrls(urls)
	# print(finalUrls)

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