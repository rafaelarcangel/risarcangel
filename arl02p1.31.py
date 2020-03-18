"""R. IÑIGO S. ARCANGEL
   DATALOG Lab02
   Feb. 5, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

#Inputing the charged amount and the payment for the charged amount
purchase = float(input("Enter Amount Charged: "))
pay = float(input("Enter Money Given: "))
#Calculating the change
change = pay - purchase
#Print the amount of change
print(change)
Thousand=int(change/1000) # Calculating if how many 1000 peso bills can be extracted
change = change%1000 # Getting the remainder
FiveHundred = int(change/500) # Calculating if how many 500 peso bills can be extracted
change = change%500 # Getting the remainder
TwoHundred = int(change/200) # Calculating if how many 200 peso bills can be extracted
change = change%200 # Getting the remainder
OneHundred = int(change/100) # Calculating if how many 100 peso bills can be extracted
change = change%100 # Getting the remainder
Fifty = int(change/50) # Calculating if how many 50 peso bills can be extracted
change = change%50 # Getting the remainder
Bente = int(change/20) # Calculating if how many 20 peso bills can be extracted
change = change%20 # Getting the remainder
Ten = int(change/10) # Calculating if how many 10 peso coins can be extracted
change = change%10 # Getting the remainder
Five = int(change/5) # Calculating if how many 5 peso coins can be extracted
change = change%5 # Getting the remainder
Piso = int(change/1) # Calculating if how many 1 peso coins can be extracted
change = change%1 # Getting the remainder
Centavo = int(change/.25) # Calculating if how many .25 centavos can be extracted
change = change%.25 # Getting the remainder

#PRINTING THE RESULTS
print("Amount of Change: ", change)
print("Number of 1000 Pesos needed: ", Thousand)
print("Number of 500 Pesos needed: ", FiveHundred)
print("Number of 200 Pesos needed: ", TwoHundred)
print("Number of 100 Pesos needed: ", OneHundred)
print("Number of 50 Pesos needed: ", Fifty)
print("Number of 20 Pesos needed: ", Bente)
print("Number of 10 Pesos needed: ", Ten)
print("Number of 5 Pesos needed: ", Five)
print("Number of 1 Peso needed: ", Piso)
print("Number of 0.5 Centavos needed: ", Centavo)
