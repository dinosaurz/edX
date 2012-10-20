# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # longer solution
    # result = 0.0
    # for i in range(len(poly)):
    #     result += poly[i] * (x ** i)
    # return result

    return float(sum([(poly[i] * (x ** i)) for i in range(len(poly))]))


# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].

    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # long solution
    derivative = []
    for i in range(len(poly)):
        if i == 0:
            continue
        nDeriv = poly[i] * i
        derivative.append(nDeriv)
    return derivative

    deriv = [float(poly[i] * i) for i in range(len(poly))]
    return deriv.remove(0.0)


# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.

    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
