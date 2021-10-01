
# Program no. 05
# Python Program to Solve Quadratic Equation
import cmath
a,b,c=map(int,input().split())
distance = (b**2) - (4 * a*c)
a1 = (-b-cmath.sqrt(distance))/(2 * a)
a2 = (-b + cmath.sqrt(distance))/(2 * a)
print(' Quadratic Equation\n',a1,a2)
