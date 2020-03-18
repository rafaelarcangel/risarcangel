"""R. IÑIGO S. ARCANGEL
   DATALOG Lab06
   March 4, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

def product(a,b): # a and b
    if (b > 0): # If b is a positive number
        return (a + product(a, b - 1))

    else:
        return 0 # Any number divided by zero is 0

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Product is: ",product(a,b))