_author_ = "Ikambarov"

position = input("Where do yopu live, E/s?: ")
address = int(input("please enter your address(Number): "))


if position == "n" or position == "E":
    if (address > 0) and (address <= 1600):
        print("You live at downtown")
    elif address <= 7200:
        print("you live at west side")
    else:
        print("You live at west suburds")
elif position == "s":
    if (address > 0) and (address <=1200):
        print("You live at downtown")
    elif address <= 9500:
        print("You at East side")
    else:
        print("You live at East subers")
