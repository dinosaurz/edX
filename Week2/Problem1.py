balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def nextMonth(prevBalance, annualRate, monthlyMin, total):
    monthlyRate = annualRate / 12.0
    monthMin = monthlyMin * prevBalance
    balance = (prevBalance - monthMin) * (1 + monthlyRate)

    print "Minimum monthly Payment: %0.2f" % (monthMin)
    print "Remaining balance: %0.2f" % (balance)

    return total + monthMin, balance


def main(balance, annualRate, monthlyRate):
    total = 0
    for month in range(12):
        print "Month:", month + 1
        total, balance = nextMonth(balance, annualRate, monthlyRate, total)
    print "Total paid: %0.2f" % (total)
    print "Remaining balance: %0.2f" % (balance)

main(balance, annualInterestRate, monthlyPaymentRate)
