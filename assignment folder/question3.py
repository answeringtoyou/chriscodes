import math
a = float(input("33: "))
b = float(input("44: "))
c = float(input("88: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of the triangle is: ", area)