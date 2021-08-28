"""
This program prints the n natural number there are two ways to do it
1.Print as 54321
2.Print as 12345

"""
# In the first program
def print_n_to_1(n):
    if(n==0):
        return
    print(n) # N is printed firsted then function call is given so it prints 5 before going to 5-1 = 4
    return print_n_to_1(n-1)

# In the 2nd Program
def print_1_to_n(n):
    if(n==0):
        return
    print_1_to_n(n-1) # Function is called first and printed later so when it traces back it comes to be 1 2 3 4 5 cox it is back tracing from the stack 
    print(n)

n = int(input("Enter the number"))
print_n_to_1(n)
print_1_to_n(n)