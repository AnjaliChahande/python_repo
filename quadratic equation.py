#program to solve the quadratic equation 
# quadratic equation is ax**2 + bx +c =  0 
# a ,  b and c are real numbers 
# a! = 0 

import cmath 

a = int(input("enter a number (a!=0) : "))
b = int(input("enter number :"))
c = int(input("enter number :"))

# formula for discriminant 

d =  b**2 - 4*a*c 

root1 = (-b-cmath.sqrt(d))/(2*a )
root2 = (-b+cmath.sqrt(d))/(2*a)

print ("the roots are", root1, "and" ,root2)
