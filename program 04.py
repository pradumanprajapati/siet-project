# Program no. 04
#Python Program to Calculate the Area of a Triangle
a,b,v=map(int,input().split())
s=(a+b+v)/2
area = (s*(s-a)*(s-b)*(s-v)) ** 0.5
print("Area of a Triangle\n",area)
