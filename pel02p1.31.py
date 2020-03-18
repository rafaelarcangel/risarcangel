""" R. COLLEEN P. PENETRANTE
   DATALOG Lab02
   Feb. 5, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""


amountCharged = float(input("Please enter the amount charged: "))
amountPay = float(input("Enter the amount you will give: "))
amountChange = amountPay - amountCharged
print("Amount:", amountChange)

A = amountChange // 1000
print("Number of 1000 peso bills:",int(A))
A_amount = amountChange % 1000

B = A_amount // 500
print("Number of 500 peso bills:",int(B))
B_amount = A_amount % 500

C = B_amount // 200
print("Number of 200 peso bills:",int(C))
C_amount = B_amount % 200

D = C_amount // 100
print("Number of 100 peso bills:",int(D))
D_amount = C_amount % 100

E = D_amount // 50
print("Number of 50 peso bills:",int(E))
E_amount = D_amount % 50

F = E_amount // 20
print("Number of 20 peso bills:",int(F))
F_amount = E_amount % 20

G = F_amount // 10
print("Number of 10 peso coins:",int(G))
G_amount = F_amount % 10

H = G_amount // 5
print("Number of 5 peso coins:",int(H))
H_amount = G_amount % 5

I = H_amount // 1
print("Number of 1 peso coins:",int(I))
I_amount = H_amount % 1

J = I_amount // 0.25
print("Number of .25 cents:",int(J))
J_amount = I_amount % 0.25