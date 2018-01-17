'''
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(n): # Converts number to string and checks palindromicness
    for i in range (len(n)):
        if n[i] != n[-i - 1]:
            return False
    return True

if __name__ == "__main__":
    big = 0

    for i in range (100, 999):
        for j in range (100, 999):
            if i * j > big and isPalindrome(str(i * j)):
                big = i * j

    print (big)
