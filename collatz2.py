import numpy
#The number we will perofrm the collatz operation on
n = 20
#Keep looping until we reach 1
#Note this will assume the collatz conjecture is true
while n ! = 1:
#Print the current value of N
    Print(n)
#Check if n is even
    if n % 2 == 0:
#If it is even divide by 2
        n = n/2
#If it is odd multiply by 3 and add 1
    else:
        n =(n * 3)+1
#Finally print the 1
print(n)


