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


from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))
PrimeList = [2]
Finished = False
PrimeSum = 0
i = 2
while Finished == False:
    if PrimeCheck(i) == True :
        PrimeSum =+ i
    if i == 2000000 :
        Finished = True
    i += 1

print(sum(PrimeList))
print(datetime.now().strftime("%H:%M:%S"))