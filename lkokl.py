_author_ = "Sadykov"

bill20 = 10
bil10 = 10
bil5 = 5
bil1 = 20

cart = 0

print("1 Chocolate - 4$")
print("2 Chips - $3")
print("3 Gum - $1")
print("4 Coke $2? ")
product = int(input("Please enter "))

if product == 1:
    cart = cart + 4
elif product == 2:
    cart = cart + 3
elif product == 3:
    cart = cart + 1
elif product == 4:
    cart = cart + 2
else:
    print("Unexpected input")

bill = input("PLease enter a bill: ")

change = bill - cart
print("You change is " + str(change))

while change > 0:
    if bil120 > 0 and change > 20:
        print("Output $20 bill")
        change = change - 20
        bill20 -= 1
    elif bill10 > 0 and change > 10:
        print("Output $10 bill")
        change = change - 10
        bill10 -= 1
    elif bill5 > 0 and change > 5:
        print("Output $10 bill")
        change = change - 5
        bill5 -= 1
    elif bill2 > 0 and change > 2:
        print("Output $10 bill")
        change = change - 2
        bill2 -= 1
    elif bill1 > 0 and change > 1:
        print("Output $10 bill")
        change = change - 1
        bill1 -= 1
    else:
        print("Error, please call custemer Suport")
        break
    count += 1
