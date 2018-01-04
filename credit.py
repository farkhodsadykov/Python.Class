
loan = int(input("Please enter loan amount: "))
monthly_paument = int(input("Plese ener monthly payment: "))
interest = float(input("Please enter yearly payment %:"))

month = 1
totol_payment = 0

while loan > 0:
    if monthly_paument <= loan:
        loan -= monthly_paument
        totol_payment += monthly_paument
    else:
        totol_payment += loan
        loan = 0
    loan = loan + (loan * interest / 100 / 12)
    print("Month {} - loan: {}".format(month, loan))
    month += 1

print("It took {} month to pay pff the loan".format(month))
print("Total payment was: {}".format(totol_payment))
