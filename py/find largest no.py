 # program to find the largest among three numberes 

num1 = int(input("enter the first number here"))
num2 = int(input("enter the second number here"))
num3 = int(input("enter the third number here"))

if (num1 >num2) and (num1 >num3) :
    print (num1, "is the largest number")
elif (num2 > num1) and (num2 > num3) :
    print (num2, "is the largest number")
else: 
    print (num3, "is the largest number")
