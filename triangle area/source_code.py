import math

def długość_odcinka(x1,y1,x2,y2):
     return math.sqrt(pow(x2-x1,2)+pow((y2-y1),2))


a = int(input('Insert a: '))
b = int(input('Insert b: '))
c = int(input('Insert c: '))
d = int(input('Insert d: '))
e = int(input('Insert e: '))
f = int(input('Insert f: '))



A = długość_odcinka(a,b,c,d)
B = długość_odcinka(c,d,e,f)
C = długość_odcinka(a,b,e,f)

S = (A + B + C) / 2

area = (S*(S-A)*(S-B)*(S-C)) ** 0.5

print('The area of the triangle is %0.1f' %area)
