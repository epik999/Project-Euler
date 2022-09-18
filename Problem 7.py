from math import sqrt

def PrimeCheck(Number) :
    if Number > 2 and Number % 2 != 0 :
        NumSqrt = round(sqrt(Number))
        Index = 0
        ExitLoop = False
        IsPrime = True
        while Index < len(PrimeList) and ExitLoop == False :
            if PrimeList[Index] > NumSqrt :
                ExitLoop = True
                
            elif Number % PrimeList[Index] == 0 :
                ExitLoop = True
                IsPrime = False
            else :
                Index += 1
        if IsPrime :
            PrimeList.append(Number)
        return IsPrime
    
    elif Number != 2 :
        return False
    else :
        return True
        
PrimeList = [2]
Finished = False
PrimeSum = 0
Primes = 0
i = 2
while Primes < 10001:
    if PrimeCheck(i) == True :
        Primes += 1
    i += 1
print(i-1)