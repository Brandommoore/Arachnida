import sys

i = 0
r = False
l = False
p = False

def active_flags(digit):
    print(digit)
    global l
    global r
    if digit == "r":
        print("hola")
        r = True
    if digit == 'l':
        print("adios")
        l = True
    if digit == 'p':
        p = True

def travel_string():
    j = 1;
    while j < len(sys.argv[i]):
        active_flags(sys.argv[i][j])
        j+=1

def is_it_flag():
    if sys.argv[i][0] == '-':
        return True
    else:
        return False

def travel_arguments():
    global i
    while i < len(sys.argv):
        if is_it_flag() == True:
            travel_string()
        i+=1

if __name__ == "__main__":
    travel_arguments()
    print(r)
    print(l)
    print(p)
