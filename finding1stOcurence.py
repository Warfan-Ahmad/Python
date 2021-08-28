"""this program tells us the place of the element which occurs first in the array we have two ways to implement it
1. By slicing the array
2. By creating a variable and incremeneting"""

def foon(a,x):
    l = len(a)
    if(l==0): # Base case if we dont have anything in the array
        return -1
    elif(a[0] == x): # if the element is presenet at first place
        return 0
    smallerarray = a[1:] # Making another array out of this array
    otput = foon(smallerarray,x) # Performing operation on the sub array

    if(otput == -1): #if the output is -1 so we dont have any element
        return -1
    else:
        return (otput+1) # if we found the element while backtracing we have to add 1 as we are slicing it the first element is being left when we do this operation so when we get back 1 gets added 3 times and we have the answer as 3


"""This oen is preferable"""

def foon2(a,x,si): # we take 3 args as the si start index will be increased without creating another array
    l = len(a)
    if(l==0): # base case
        return -1
    if(a[si]==x): # here we return direct the si as that will be equal to that index arr[si] == arr[0]
        return si
    return foon2(a,x,si+1) # Here is the increment for si 

a = [1,2,3,4,5,6]
x = 4
si = 0
print(foon(a,x))
print(foon2(a,x,si))