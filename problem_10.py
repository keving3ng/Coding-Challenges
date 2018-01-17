'''
Problem 10 - Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False

    for i in range (3, n // 2, 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    i = 2
    t = 0

    while i < 2000000:
        if isPrime(i):
            t += i
        i += 1

    print(t)
