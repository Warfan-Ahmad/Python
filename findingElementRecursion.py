

def findNum(arr,key,si):
    leng = len(arr)
    if(si==leng):#Base Case if leng is equal to start index
        return 0
    if(arr[si]== key): #If si is equal to key then return si
        return si
    else:
        return findNum(arr,key,si+1) #here we increment the start index

arr = [1,2,3,4,5,6]
si = 0
key = 5
print(findNum(arr,key,si))