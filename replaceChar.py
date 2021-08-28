"""
This program replaces the item a with b
The approach used is we find the element using slicing and returing the string set
"""

def replaceChar(charset,a,b):
    if(len(charset)==0): #Base case for the program
        return charset
    
    smallercharset = replaceChar(charset[1:],a,b) # Recursive calls with slicing the character set as the characters set are immutable we have to create a new instance for it
    if(charset[0] == a): 
        return b + smallercharset # if item is found then we replace it with b and add the other half of character set
    else:
        return charset[0] + smallercharset # if item isnt found we return the element at first with other remaining half

print(replaceChar("abcddedf",'d','x'))
