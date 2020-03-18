"""R. IÑIGO S. ARCANGEL
   DATALOG Lab07
   March 18, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

def missingelement(array, first, last):
    if (first > last): # If first is greater than last, return last + 1
        return last + 1
    if (first != array[first]): # If first is not equal to array[first] return first
        return first
    x = int((first + last) / 2) # Finding x
    # from 0 to mid which is x
    if (array[x] == x):
        return missingelement(array, x + 1, last)


A = [0, 1, 2, 3, 6, 10, 11, 17] # The given sorted array
n=len(A)
print("[0, 1, 2, 3, 6, 10, 11, 17]")
print("The smallest missing element from the given array is: ", missingelement(A, 0, n-1)) #Printing the smallest missing element
print("----------------------------------------------------------")

A1 = [1, 2, 3, 4, 6, 11, 17]
n=len(A1)
print("[1, 2, 3, 4, 6, 11, 17]")
print("The smallest missing element from the given array is: ", missingelement(A1, 0, n-1)) #Printing the smallest missing element
print("----------------------------------------------------------")

A2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n=len(A2)
print("[0, 1, 2, 3, 4, 5, 6, 7, 8]")
print("The smallest missing element from the given array is: ", missingelement(A2, 0, n-1)) #Printing the smallest missing element