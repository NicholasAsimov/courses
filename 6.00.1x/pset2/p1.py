monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0
currentBalance = balance

for month in range (12):
    minimumMonthlyPayment = monthlyPaymentRate * currentBalance
    monthlyUnpaidBalance = currentBalance - minimumMonthlyPayment
    currentBalance = monthlyUnpaidBalance  + (monthlyInterestRate * monthlyUnpaidBalance)
    totalPaid += minimumMonthlyPayment

    print "Month:", month + 1
    print "Minimum monthly payment:", round(minimumMonthlyPayment, 2)
    print "Remaining balance:", round(currentBalance, 2)

print "Total paid", round(totalPaid, 2)
print "Remaining balance:", round(currentBalance, 2)
