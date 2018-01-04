#########################################################################################################
balance = 500
while True:
    print("Menu: ")6
    print("1 Deposit")
    print("2 withdrawal")
    print("3 Balance")
    menu = int(input("plese choose one of above: "))

    if menu == 1:
        deposit = int(input('How much would you like to deposit: '))
        balance = balance + deposit
        print("Your balance is ${}".format(balance))

    elif menu == 2:
        credit = int(input('How much would you like to withdraw: '))
        print("Your balance is ".format(balance))

        if credit <= balance:
             print("Here is your ${}".format(credit))

             balance = balance - credit

             print("Your balance is ${}".format(balance))
        else:
             print("Your balance is less then credit amount")
             print("Your balance is ${}".format(balance))
    elif menu == 3:
        print("Your balance is ${}".format(balance))
#########################################################################################################



















