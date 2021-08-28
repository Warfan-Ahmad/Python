

def lastIndex(arr,key):
    l = len(arr)
    if(l == 0):
        return -1
    smallerarray = arr[1:]
    output = lastIndex(smallerarray,key)
    if(output!=-1):
            return output + 1
    else:
        if(arr[0] == key):
            return 0
        else:
            return -1

def lastIndex2(arr,key,si):
    l2 = len(arr)
    if(si==l):
        return 0
    out = lastIndex2(arr,key,si+1)
    if(out!=-1):
        return si
    else:
        return -1

arr = [1,2,3,5,3]
key = 3
si = 0
print(lastIndex(arr,key))
print(lastIndex2(arr, key, si))


