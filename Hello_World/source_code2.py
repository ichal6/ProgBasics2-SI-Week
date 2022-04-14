import sys

def Hello():
    if len(sys.argv) >= 2:
        #name = sys.argv[1]
        #sys.argv.pop(0)
        string = (" ").join(sys.argv[1:])
        #print(string)
        print("Hello " + string + "!")
    
    else:
        print("Hello World!")

Hello()