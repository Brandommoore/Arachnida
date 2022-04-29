import sys
import exifread
from PIL import Image
from PIL.ExifTags import TAGS

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
	print(bcolors.YELLOW + img + bcolors.GRAY + " data EXIF:\n" + bcolors.RESET)
	imagen = Image.open(img)
	exif_data = imagen.getexif()
	exif_dic = {}
	for tag_id, value in exif_data.items():
		tag = TAGS.get(tag_id, tag_id)
		valor = exif_data.get(tag_id)
		exif_dic[tag] = valor
		print(bcolors.TURQUOISE + str(tag) + " : " + bcolors.PURPLE + str(value) + bcolors.RESET)

def extractEXIF_nonjpg():
	imagen = open("ejemplo.jpg", 'rb')
	valores_exif = exifread.process_file(imagen)
	for tag in valores_exif.keys():
	    print(str(tag) + " : " + str(valores_exif[tag]))

if __name__ == "__main__":

	#print(bcolors.GREEN + "File Open Successfully!" + bcolors.RESET)
	extractEXIF("Telos_Portada_118.jpeg")

