
def calculate():
    import sys # Will be used for terminating the program
    num1 = float(input("Enter 1st number: ")) # Input 1st number
    num2 = float(input("Enter 2nd number: ")) # Input 2nd number
    operation = input(" + = Add \n - = Subtract \n * = multiply \n / = divide \n") # Displaying types of operations and their corresponding symbol
    if operation == "+": # If "+" is the inputted operator, addition will be conducted
        answer = num1+num2
    elif operation == "-": # If "-" is the inputted operator, subtraction will be conducted
        answer = num1-num2
    elif operation == "*": # If "*" is the inputted operator, multiplication will be conducted
        answer = num1*num2
    elif operation == "/": # If "/" is the inputted operator, division will be conducted
        answer = num1/num2
    else:
        print("ERROR, Please type an operator") # It will be displayed if the inputted character was not a given option
        sys.exit() # It will terminate the program already
    print(float(answer)) # It will display the answer if the conditions were met successfully

    again() # To Calculate again

def again(): # Function needed to calculate again
    calculate()
    again()
calculate()

