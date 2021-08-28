"""
This program calculates the sum of the array elemets 
The approach i used was i started from the last element and came to the first element 
and calculated the result 

"""
def sumArray(arr,leng):
    if(leng == 0): #Base case if we dont have any element in the array 
        return 0

    return arr[leng-1] + sumArray(arr,leng-1)
#leng is 3 and we start from 2 as the index starts from 2 1 0 & and we add the recursion function and we start from leng-1
arr = [1,2,3,4,5]
leng = len(arr)

print(sumArray(arr,leng))