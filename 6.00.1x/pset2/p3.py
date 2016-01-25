def endYearBalance(balance, annualInterestRate, monthlyPayment):
    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(12):
        monthlyInterest = balance * monthlyInterestRate
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    return balance

initialBalance = balance
lower = initialBalance / 12
upper = (initialBalance * (1 + annualInterestRate / 12.0)**12) / 12.0
monthlyPayment = (lower + upper) / 2.0
calculatedBalance = endYearBalance(initialBalance, annualInterestRate, monthlyPayment)

while round(calculatedBalance) != 0:
    if calculatedBalance > 0:
        lower = monthlyPayment
    elif calculatedBalance < 0:
        upper = monthlyPayment

    monthlyPayment = (lower + upper) / 2.0
    calculatedBalance = endYearBalance(initialBalance, annualInterestRate, monthlyPayment)

print "Lowest Payment:", round(monthlyPayment, 2)
