import sys
from soup import *
from download import *
import requests

#[reverse, level, path, url]
datos = [False, 5, './data/', ' ']
args = sys.argv

def travel_arguments(datos, args):
    i = 0
    while i < len(sys.argv):
        if args[i] == '-r':
            datos[0] = True
        elif args[i] == '-l':
            datos[1] = args[i+1]
            i+=1
        elif args[i] == '-p':
            datos[2] = args[i+1]
            i+=1
        i+=1
    print(args[i-1])
    datos[3] = sys.argv[i-1]

if __name__ == "__main__":
    travel_arguments(datos, args)
    path = datos[2]
    # I changed the fuction by a newer fuction who return all urls
    #print(datos[3])
    #print(datos[1])
    urls = startHunting(datos[3], int(datos[1]))
    for url in urls:
        try:
            download(url, path)
        except Exception as e:
            pass