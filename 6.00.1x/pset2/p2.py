# Test Case 1:
balance = 3329
annualInterestRate = 0.2

def endYearBalance(balance, annualInterestRate, monthlyPayment):
    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(12):
        monthlyInterest = balance * monthlyInterestRate
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    return balance

initialBalance = balance
monthlyPayment = 10
calculatedBalance = endYearBalance(initialBalance, annualInterestRate, monthlyPayment)

while calculatedBalance >= 0:
    monthlyPayment += 10
    calculatedBalance = endYearBalance(initialBalance, annualInterestRate, monthlyPayment)

print "Lowest Payment:", monthlyPayment
