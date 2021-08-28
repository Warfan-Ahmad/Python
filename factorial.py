"""This program performs the factorail operation on a number"""

def fact(n):
    if(n==1): #This is the base case
        return 1
    return n * fact(n-1) # Fact(n-1) is decrementing the number by one in order to get the one number less than one

n = int(input("Enter the Number for factorail"))
output = fact(n)
print(output)


