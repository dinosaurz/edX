balance = 999999
annualInterestRate = 0.18


def nextMonth(prevBalance, annualRate, monthMin):
    monthlyRate = annualRate / 12.0
    return (prevBalance - monthMin) * (1 + monthlyRate)


def oneYear(balance, annualRate, payment):
    for month in range(12):
        balance = nextMonth(balance, annualRate, payment)
    return balance


def main(balance, annualRate):
    newBalance = balance
    payment = 0

    while newBalance > 0:
        payment += 0.01
        newBalance = oneYear(balance, annualRate, payment)

    print "Lowest Payment: %0.2f" % (payment)

main(balance, annualInterestRate)
