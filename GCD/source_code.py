import sys


if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
else:
    sys.exit()    

temp = 0

while b !=0:
    temp = b
    b = a%b
    a = temp

print(a)