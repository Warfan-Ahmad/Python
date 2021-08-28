"""
This program removes the character from the string if it is found.
"""

def removeChar(charset,key): 
    if(len(charset)==0): # Base case if we dont have any character in the charset return empty charset
        return charset
    smallerOutput = removeChar(charset[1:],key) # slicing as we they are immutable

    if(charset[0]==key): # if the first element is equal to the key meaning that the first element of the smaller charset is equal to the key then we only return the half without that element
        return smallerOutput
    else:
        return charset[0] + smallerOutput # if we didnt found then we return the element and other half


print(removeChar("abxxcxafdasdxxfasxxxfsadfxx",'x'))