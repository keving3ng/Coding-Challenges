'''
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

if __name__ == "__main__":
    a = 1
    b = 0
    i = 1
    t = 0

    while len(str(a)) != 1000:
        t = a + b
        b = a
        a = t
        i += 1
        
    print (i)
