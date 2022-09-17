# https://projecteuler.net/problem=5

AnswerFound = False
TestNumber = 1
DivisbleUntil = 20
while AnswerFound == False :
    DivisibleBy = []
    if TestNumber % 20 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 18 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 16 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 14 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 12 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 15 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 17 != 0 :
        TestNumber += 1
        continue
    if TestNumber % 19 != 0 :
        TestNumber += 1
        continue
    DivisibleBy.append(1)
    DivisibleBy.append(2)
    DivisibleBy.append(3)
    DivisibleBy.append(4)
    DivisibleBy.append(5)
    DivisibleBy.append(6)
    DivisibleBy.append(7)
    DivisibleBy.append(8)
    DivisibleBy.append(9)
    DivisibleBy.append(10)
#    DivisibleBy.append(11)
    DivisibleBy.append(12)
#    DivisibleBy.append(13)
    DivisibleBy.append(14)
    DivisibleBy.append(15)
    DivisibleBy.append(16)
    DivisibleBy.append(17)
    DivisibleBy.append(18)
    DivisibleBy.append(19)
    DivisibleBy.append(20)
#    print(DivisibleBy)
    for x in range(1,DivisbleUntil+1) :
        if x in DivisibleBy :
            continue
        print(TestNumber, x)
        if TestNumber % x == 0 :
            DivisibleBy.append(x)
            if len(DivisibleBy) == DivisbleUntil :
                AnswerFound = True
        elif TestNumber % x != 0 :
            TestNumber += 1
            break   
print(TestNumber, "is divisble by", DivisibleBy)