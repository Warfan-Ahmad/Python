
"""This program evaluates the power of a number using recursion"""

def power(num,pow):
    if(pow == 0): #This is the base case
        return 1
    elif(pow < 0): # Constraint if we have wrong input
        return -1
    elif(pow==0 & num == 0): # If both are 0 
        return 1 
    smallOutput = power(num,pow-1) # reducing the power to small pieces
    return num * smallOutput #calculating the answer

n = int(input("Enter the number"))
pow = int(input("Enter the power"))

output = power(n,pow)
print(output)