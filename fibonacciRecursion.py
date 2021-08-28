"""This program prints the fibonacci number at n"""



def fib(n):
    if(n == 1 or  n == 2): #this is base case as if n==1 that means only 1 is there in the fibonacci series and at 2nd there is also one and then 1+1 = 2 that is 3rd fibonacci number
        return 1

    return fib(n-1) + fib (n-2) #Here we are calling function two times as we know that the sum is equal to the previous two numbers in the series

n = int(input("Enter no"))
print(fib(n))