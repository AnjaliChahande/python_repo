# program to find the factorial of a number 

num = int(input("enter a number here: " ))

fact =1

if num < 0:
    print("factorial does not exits")
if num ==0: 
    print ("factorial of 0 is ", 1)
if num >0 :
    for i in range (1, num+1)
    fact = fact+1
print ("the factorial of the given number is ", fact)