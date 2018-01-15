
from numberfunctions import isPrime

n = int(input("n = "))

i = n // 2
found = False

while found == False:
    i = i - 2
    if isPrime(i) and n % i == 0:
        found = True
    
        
print ("The largest prime factor of",str(n),"is", str(i))
