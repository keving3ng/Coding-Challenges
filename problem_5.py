"""
Problem 5 - Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isDiv(n):
    divvy = True
    for i in range(2, 20):
        if n % i != 0:
            divvy = False

    return divvy

i = 2520
while isDiv(i) is False:
    i += 20

print ("Result = ", str(i))
