n = 999

register = 0
while (n > 100) and (register != 25):
    if (n%7 == 0) or (n%9 == 0):
        
        
        register+=1
        print(str(register) + ".  ",end="")
        print(n)
        n-=1
    else:
        n-=1

