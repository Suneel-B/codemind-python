a,b,c=map(int,input().split())
s=(a+b+c)/2
from math import sqrt
ar=sqrt(s*(s-a)*(s-b)*(s-c))
print("{0:.2f}".format(ar))