import sys

# args = len(sys.argv);
i = 0
while i < len(sys.argv):
    if sys.argv[i][0] == '-':
        print(sys.argv[i])
        print("es un flag")
    i+=1