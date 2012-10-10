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
    monthlyMin = balance / 12.0
    monthlyMax = oneYear(balance, annualRate, 0) / 12
    epsilon = 0.001

    while monthlyMin < monthlyMax:
        payment = (monthlyMin + monthlyMax) / 2.0
        newBalance = oneYear(balance, annualRate, payment)
        if abs(newBalance) < epsilon:
            break
        elif newBalance > 0:
            monthlyMin = payment
        else:
            monthlyMax = payment

    print "Lowest Payment: %0.2f" % (payment)

main(balance, annualInterestRate)
