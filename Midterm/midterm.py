def laceStrings(s1, s2):
    news = []
    inner = min(len(s1), len(s2))
    if inner == len(s1):
        outer = len(s2)
    else:
        outer = len(s1)

    for i in range(inner):
        news.append(s1[i])
        news.append(s2[i])
    if outer > inner:
        if outer == len(s1):
            news.append(s1[inner:])
        else:
            news.append(s2[inner:])

    return ''.join(news)


def laceStringsRecur(s1, s2):
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')


def McNuggets(n):
    # Create the list of falses
    trues, falses = [0], []
    i, successes = 1, 0

    while True:
        if i - 6 in trues or i - 9 in trues or i - 20 in trues:
            trues.append(i)
            successes += 1
            if successes == 6:
                break
        else:
            falses.append(i)
            successes = 0
        i += 1

    if n in falses:
        return False
    return True


def fixedPoint(f, epsilon):
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


def babylon(a):
    def test(x):
        return 0.5 * (a / x + x)
    return fixedPoint(test, 0.0001)


def sqrt(a):
    return babylon(a)
