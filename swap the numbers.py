#program for swap the numbers 

#swap number using 3 rd variable 

#a= 2
#b =3

#x = a 
#a= b
#b= x 

x = input("enter the value of x: ")
y = input("enter the value of y:")

temp = x
print ("now the value of temp variable is ", temp)

x=y 
print ("now the value of x is ", x)

y = temp
print ("the value of y is ", y)

#swap numbers without using 3rd variable

x = input("enter the value of x : ")
y = input ("enter the value of y : ")

x, y = y, x

print ("the value of x is " ,x)
print ("the value of y is ", y)