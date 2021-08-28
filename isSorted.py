"""THis program checks if the given list is sorted or not"""

def isSorted(n,i):
    l = len(n) 
    if(i==l or i==l-1): #Here the main base case is l-1 which is length -1 which will work for i+1 in the elif condition otherwise that will get out of bound.......the first condition is for if the array has only one element in it.
        return True
    elif(n[i] > n[i+1]): #simple check for greater or not
        return False
    
    return isSorted(n,i+1) # giving i+1 as we have to neglect the first element now as that is already sorted

n = [1,2,3,4,5,6,87,8,9]
i = 0
print(isSorted(n,i))