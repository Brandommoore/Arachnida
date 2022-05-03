import sys
import os
import exifread
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from libxmp.utils import file_to_dict
from libxmp import consts

class bcolors:
	RESET='\033[0m'
	GREEN='\033[1;32m'
	RED='\033[0;31m'
	BLUE='\033[0;34m'
	YELLOW='\033[1;33m'
	PURPLE='\033[0;35m'
	TURQUOISE='\033[0;36m'
	GRAY='\033[0;37m'

i = 0
while i < len(sys.argv):
	if sys.argv[i][0] == '-':
		print(sys.argv[i])
		print("es un flag")
	i+=1

def extractEXIF(img):
	try:
		imagen = Image.open(img)
		exif_data = imagen.getexif()
		if not exif_data:
			print(bcolors.RED + "No metadata finded in " + bcolors.YELLOW + img + bcolors.RESET)
		else:
			print(bcolors.YELLOW + img + bcolors.GRAY + " data EXIF:\n" + bcolors.RESET)
			exif_dic = {}
			for tag_id, value in exif_data.items():
				tag = TAGS.get(tag_id, tag_id)
				valor = exif_data.get(tag_id)
				exif_dic[tag] = valor
				print(bcolors.TURQUOISE + str(tag) + " : " + bcolors.PURPLE + str(value) + bcolors.RESET)
			print("\n")
			img.close()
	except Exception as e:
		pass

def extractEXIF_png_gif(img_name):
	try:
		img = Image.open(img_name)
		xmp_data = file_to_dict(img_name)
		if not xmp_data:
			print(bcolors.RED + "No metadata finded in " + bcolors.YELLOW + img_name + bcolors.RESET)
		else:
			print(bcolors.YELLOW + img_name + " data XMP:\n" + bcolors.RESET)
			data = xmp_data[consts.XMP_NS_DC]
			print(bcolors.GREEN + data[0][0] + bcolors.RESET)
			print(bcolors.GREEN + data[0][1] + bcolors.RESET)
			for key, value in data[0][2].items():
				print(bcolors.TURQUOISE + str(key) + " : " + bcolors.PURPLE + str(value) + bcolors.RESET)
			print("\n")
		img.close()
	except Exception as e:
		print(bcolors.RED + "Error\n" + bcolors.RESET)
		pass

def scorpionEXTRACTER(img_name):
	if img_name.endswith((".jpg", ".jpeg")):
		extractEXIF(img_name)
	elif img_name.endswith((".png", ".gif", ".bpm")):
		extractEXIF_png_gif(img_name)
	else:
		print(bcolors.RED + "File extension not supported\n" + bcolors.RESET)

def cleanProgName(arguments):
	progName=arguments[0]
	for arg in arguments:
		if arg is progName:
			arguments.remove(arg)
	return(arguments)

if __name__ == "__main__":
	arguments=[]
	arguments=sys.argv
	arguments=cleanProgName(arguments)
	for img in arguments:
		scorpionEXTRACTER(img)

