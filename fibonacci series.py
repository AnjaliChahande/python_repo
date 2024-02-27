# fibonacci series program 

#logic first no is 1 2nd no is 2 then 3rd no will be the sum of first no and secnond no that is 1 +2 = 3 
# a = 0  b= 1 
# 0+1=1 
#1+1=2 , 2+1 = 3 , 3+2= 5

a =0 
b= 1

num = int(input("enter a number to obtain fibonacci series : " ))

if num ==1:
    print(a)
else :
    print(a)
    print(b)
    for i in range( 2, num) :
        C = a+b
        a=b
        b=C
        print (C)

        

