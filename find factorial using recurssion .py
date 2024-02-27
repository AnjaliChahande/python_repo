# program to find the factorial of a number using recurssion 

def fact(a):
    if a ==0 :
        return 1 
    else:
        return ((a)*fact(a-1))

num= int(input("enter a number here: "))
result = fact(num)
print ("the factorial of the given number is ", result)

