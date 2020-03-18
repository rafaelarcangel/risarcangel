print("Welcome to Ramzi Food and Tapsi\n")
print("Main Dish\nTapsilog\tP75\nBacsilog\tP79\nTocilog\tP70\nHotsilog\tP70\nLongsilog\tP70\nBangsilog\tP75\n")
print("Drinks\nCoke\tP25\nSprite\tP25\nIced Tea\tP30\nMango Shake\tP50\nChocolate Shake\tP45\nSago't Gulaman\tP15\n")
print("Desserts\nLeche Flan\tP20\nHalo-halo\tP30\nBuko Pandan\tP25\nMais con yelo\tP27\n")
print("Add-ons\nRice\tP15\nEgg\tP10\nExtra Bacon\tP40\nCheese Sauce\tP10\nFries\tP35\n")
print("Burgers/Sandwiches\nHamburger\tP30\nCheeseburger\tP35\nCheeseburger w/ egg\tP42\nDouble Cheeseburger\tP40\nClubhouse\tP50\n")
print("Note:\tFor every at least 200 pesos worth of purchase, you get a 15% discount.\n")
var1 = str(input("What is your order?\t"))
if (var1 == "Tapsilog"):
    var1 = 75
elif (var1 == "Bacsilog"):
    var1 = 79
elif (var1 == "Tocilog"):
    var1 = 70
elif (var1 == "Hotsilog"):
    var1 = 70
elif (var1 == "Longsilog"):
    var1 = 70
elif (var1 == "Bangsilog"):
    var1 = 75
elif (var1 == "None"):
    var1 = 0
else:
    print("Sorry it's unvailable")

var2 = str(input("What is your drinks?\t"))
if (var2 == "Coke"):
    var2 = 25
elif (var2 == "Sprite"):
    var2 = 25
elif (var2 == "Iced Tea"):
    var2 = 30
elif (var2 == "Mango Shake"):
    var2 = 50
elif (var2 == "Chocolate Shake"):
    var2 = 45
elif (var2 == "Sago't Gulaman"):
    var2 = 15
elif (var2 == "None"):
    var2 = 0
else:
    print("Sorry it's unvailable")

var3 = str(input("Any desserts?\t"))
if (var3 == "Leche Flan"):
    var3 = 20
elif (var3 == "Halo-halo"):
    var3 = 30
elif (var3 == "Buko Pandan"):
    var3 = 25
elif (var3 == "Mais con yelo"):
    var3 = 27
elif (var3 == "None"):
    var3 = 0
else:
    print("Sorry it's unvailable")

var4 = str(input("Any additional?\t"))
if (var4 == "Rice"):
    var4 = 15
elif (var4 == "Egg"):
    var4 = 10
elif (var4 == "Extra Bacon"):
    var4 = 40
elif (var4 == "Cheese Sauce"):
    var4 = 10
elif (var4 == "Fries"):
    var4 = 35
elif (var4 == "None"):
    var4 = 0
else:
    print("Sorry it's unvailable")

var5 = str(input("How about you try our burger/sandwich, anything you like?\t"))
if (var5 == "Hamburger"):
    var5 = 30
elif (var5 == "Cheeseburger"):
    var5 = 35
elif (var5 == "Cheeseburger w/ egg"):
    var5 = 42
elif (var5 == "Double Cheeseburger"):
    var5 = 40
elif (var5 == "Clubhouse"):
    var5 = 50
elif (var5 == "None"):
    var5 = 0
else:
    print("Sorry it's unvailable")

Total = var1+var2+var3+var4+var5
var6 = str(input("Are you a senior citizen/PWD?\t"))
if (var6 == "yes") and Total >= 200:
    var6 = (int(Total) * 0.20)
    DiscountedPrice = Total - var6
    Discount_15 = (int(DiscountedPrice) * 0.15)
    SuperDiscountedPrice = (int(DiscountedPrice - Discount_15))
    print("\nThank you for ordering!\nYour total bill is:", float(SuperDiscountedPrice))
if (var6 == "yes") and Total < 200:
    var6 = (int(Total) * 0.20)
    DiscountedPrice = (int(Total - var6))
    print("\nThank you for ordering!\nYour total bill is:", float(DiscountedPrice))
if (var6 == "no") and Total >= 200:
    var6 = (int(Total) * 0.15)
    Discount_NoPWD = (int(Total - var6))
    print("\nThank you for ordering!\nYour total bill is:", float(Discount_NoPWD))
if (var6 == "no") and Total < 200:
    print("\nThank you for ordering!\nYour total bill is:", int(Total))


print("\nEnjoy your meal!")