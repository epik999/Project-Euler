# https://projecteuler.net/problem=3

Number = 600851475143
for x in range(2, Number+1) :
    if Number%x == 0: 
        IsPrime = True 
        for y in range(2,(x//2 + 1)): 
            if x % y == 0 :
                IsPrime = False
                break
        if IsPrime == True:
            print(x, end=', ')