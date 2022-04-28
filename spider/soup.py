from operator import truediv
import sys
import time
import urllib.request
from cgitb import html
from bs4 import BeautifulSoup

# - img_routes -- return: whole list of images
# - check_images -- returm: correct url list images
#

# cleanUrlList - return: list without duplicates
# chech if url in cleanList already exist
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
		time.sleep(0.1)
	return(allUrls)

# def recursiveFindUrls(listUrls, depth, current_depth):
# 	allUrls=[]
# 	#listUrls=url
# 	current_depth+=1
# 	if current_depth <= depth:
# 		allUrls=urlLooper(listUrls)
# 		return(allUrls, depth, current_depth)
# 	allUrls=recursiveFindUrls(allUrls, depth, current_depth)
# 	return(allUrls)

# def recursiveFindUrls(listUrls, depth, current_depth):
# 	allUrls=[]
# 	#listUrls=url
# 	current_depth+=1
# 	if current_depth <= depth:
# 		allUrls=recursiveFindUrls(listUrls, depth, current_depth)
# 	return(allUrls)

def recursiveFindUrls(url, depth, current_depth):
	listUrls=[]
	#listUrls=url
	listUrls.append(url)
	# print(len(listUrls[:]))
	# print(listUrls)
	# if depth==0:
	# 	return([])
	if len(listUrls[:]) == 1:
		#print(listUrls)
		listUrls.extend(findUrls(listUrls))
	while current_depth <= depth:
		listUrls.extend(urlLooper(listUrls))
		listUrls=sanitizeUrls(listUrls)
		current_depth+=1
	return(listUrls)

if __name__ == "__main__":

	url = sys.argv[1]
	depth = int(sys.argv[2])
	#urls=[]
	#urls.append(url)
	# img_routes(url)
	# allUrls=findUrls(url)
	# allUrls=recUrls(allUrls)
	# print(allUrls)

	#print(findUrls(url))
	print("Spider is hunting urls...")
	allUrls=recursiveFindUrls(url, depth, 0)
	#print(allUrls)
	print("Spider is hunting images...")
	allImgs=findImages(allUrls)
	print(allImgs)


	#print(urlLooper(findUrls(url)))

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