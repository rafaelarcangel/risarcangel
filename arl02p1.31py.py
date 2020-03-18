x = float(input("Enter Amount Charged: "))
y = float(input("Enter Money Given: "))

a = y - x

OneThousand = a//1000
money = a%1000
FiveHundred = a//500
money = a%500
TwoHundred= a//200
money = a%200
OneHundred = a//100
money = a%100
Fifty = a//50
money = a%50
Bente = a//20
money = a%20
Ten = a//10
money = a%10
Five = a//5
money = a%5
Piso = a//1
money = a%1
Centavo = a//0.5
money = a%0.5

print("Number of 1000 Pesos needed: ", OneThousand)
print("Number of 500 Pesos needed: ", FiveHundred)
print("Number of 100 Pesos needed: ", OneHundred)
print("Number of 50 Pesos needed: ", Fifty)
print("Number of 20 Pesos needed: ", Bente)
print("Number of 10 Pesos needed: ", Ten)
print("Number of 5 Pesos needed: ", Five)
print("Number of 1 Peso needed: ", Piso)
print("Number of 0.5 Centavos needed: ", Centavo)

