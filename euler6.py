# Project Euler Problem 6

def sumOfSquares(n):
    sum = 0
    for i in range (1, n+1):
        sum += (i ** 2)

    return sum

def squareOfSum(n):
    sum = 0
    for i in range (1, n+1):
        sum += i

    return (sum**2)

if __name__ == "__main__":
    a, b = sumOfSquares(100), squareOfSum(100)
    c = abs(a - b)
    print (str(a)," - ", str(b)," = ", str(c))
