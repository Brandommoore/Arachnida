import sys
import os
import exifread
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from libxmp.utils import file_to_dict # Module for XMP metadata manipulation
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

# args = len(sys.argv);
i = 0
while i < len(sys.argv):
	if sys.argv[i][0] == '-':
		print(sys.argv[i])
		print("es un flag")
	i+=1

def extractEXIF(img):
	try:
		print(bcolors.YELLOW + img + bcolors.GRAY + " data EXIF:\n" + bcolors.RESET)
		imagen = Image.open(img)
		exif_data = imagen.getexif()
		exif_dic = {}
		for tag_id, value in exif_data.items():
			tag = TAGS.get(tag_id, tag_id)
			valor = exif_data.get(tag_id)
			exif_dic[tag] = valor
			print(bcolors.TURQUOISE + str(tag) + " : " + bcolors.PURPLE + str(value) + bcolors.RESET)
	except Exception as e:
		print(bcolors.RED + "Error\n" + bcolors.RESET)
		pass

def extractEXIF_png_gif(img_name):
	img = Image.open(img_name)
	xmp_data = file_to_dict(img_name)
	if not xmp_data:
		print(bcolors.RED + "No metadata finded" + bcolors.RESET)
	else:
		data = xmp_data[consts.XMP_NS_DC]
		print(data[0][0])
		print(data[0][1])



if __name__ == "__main__":

	#print(bcolors.GREEN + "File Open Successfully!" + bcolors.RESET)
	extractEXIF("42-Barcelona-Conjunto.jpg")
	# extractEXIF_nonjpg("bicimad.png")

