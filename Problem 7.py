def PrimeCheck(Number) :
    for x in range(2, Number) :
        if Number % x == 0 :
            return False
    return True

Primes = 0
i = 2
while Primes < 10001:
    if PrimeCheck(i) == True :
        Primes += 1
    i += 1
print(i-1)
