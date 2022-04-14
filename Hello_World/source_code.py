import sys

def Hello():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        print("Hello " + name + "!")
    
    else:
        print("Hello World!")

Hello()