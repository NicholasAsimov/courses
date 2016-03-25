import matplotlib.pyplot as pylab

principal = 10000
interestRate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate

pylab.plot(range(years + 1), values, linewidth=3)
pylab.title('5% Growth, Compaunded Annually')
pylab.xlabel('Years or Compounding')
pylab.ylabel('Value of Principal ($)')
pylab.show()
