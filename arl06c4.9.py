"""R. IÑIGO S. ARCANGEL
   DATALOG Lab06
   March 4, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

def findMin(A, x): #Defining the function for finding the Minimum
    if (x == 1):
        return A[0] # if size is equal to 0, it means whole array
    return min(A[x - 1], findMin(A, x - 1)) # Returning minimum value

def findMax(A, x): #Defining the function for finding the Maximum
    if (x == 1):
        return A[0]  # if size is equal to 0, it means whole array
    return max(A[x - 1], findMax(A, x - 1)) # Returning maximum value

if __name__ == "__main__": #DriverCode
    A = [50, 100, 62, -6, -60, 102, 31] # The List for A
    x = len(A)
    print(findMax(A, x)) #Printing Maximum Value
    print(findMin(A, x)) #Printing Minimum Value  