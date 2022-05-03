from operator import truediv
import sys
import time
import urllib.request
from cgitb import html
from bs4 import BeautifulSoup

def cleanDupList(urlList):
	cleanList=[]
	for url in urlList:
		if url not in cleanList:
			cleanList.append(url)
	return(cleanList)

def checkUrls(urlList):
	avoid=((None, 'None', '#', '/', '', ' '))
	for url in urlList:
		if url in avoid:
			urlList.remove(url)
	return(urlList)

def sanitizeUrls(urlList):
	urlList=cleanDupList(urlList)
	urlList=checkUrls(urlList)
	return(urlList)

def imgRoutes(url):
	img_url=[]
	try:
		datos = urllib.request.urlopen(url)
		soup = BeautifulSoup(datos, "html.parser")
		tags = soup('img')
		for tag in tags:
			img_url.append(tag.get('src'))
		img_url=cleanDupList(img_url)
		return(img_url)
	except Exception as e:
		return([])
		pass

def checkImages(img_url):
	myImgs=[]
	suffix=((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
	for elem in img_url:
		if elem.endswith(suffix):
			myImgs.append(elem)
	return(myImgs)

def findImages(listUrls):
	images=[]
	for url in listUrls:
		images.extend(imgRoutes(url))
	images=sanitizeUrls(images)
	images=checkImages(images)
	return(images)

def findUrls(url):
	myUrls=[]
	try:
		data=urllib.request.urlopen(url)
		soup=BeautifulSoup(data, "html.parser")
		tags=soup('a')
		for tag in tags:
			myUrls.append(tag.get('href'))
		myUrls=sanitizeUrls(myUrls)
		return(myUrls)
	except Exception as e:
		return([])
		pass

def urlLooper(listUrls):
	allUrls=[]

	for url in listUrls:
		currentUrls=findUrls(url)
		allUrls.extend(currentUrls)
		time.sleep(0.01)
	return(allUrls)

def recursiveFindUrls(url, depth, current_depth):
	listUrls=[]
	listUrls.append(url)
	if len(listUrls[:]) == 1:
		#print(listUrls)
		listUrls.extend(findUrls(listUrls))
	while current_depth <= depth:
		listUrls.extend(urlLooper(listUrls))
		listUrls=sanitizeUrls(listUrls)
		current_depth+=1
	return(listUrls)

def startHunting(url, depth):
	print("Spider is hunting urls...")
	allUrls=recursiveFindUrls(url, depth, 0)
	print("Spider is hunting images...")
	allImgs=findImages(allUrls)
	return(allImgs)

# if __name__ == "__main__":

# 	url = sys.argv[1]
# 	depth = int(sys.argv[2])

# 	print("Spider is hunting urls...")
# 	allUrls=recursiveFindUrls(url, depth, 0)
# 	print("Spider is hunting images...")
# 	allImgs=findImages(allUrls)
# 	print(allImgs)
