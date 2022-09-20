# https://projecteuler.net/problem=5

AnswerFound = False
TestNumber = 1
DivisbleUntil = 20
while AnswerFound == False :
    if TestNumber % 20 != 0 and TestNumber % 18 != 0 and TestNumber % 16 != 0 and TestNumber % 14 != 0 and TestNumber % 12 != 0 and TestNumber % 15 != 0 and TestNumber % 17 != 0 and TestNumber % 19 != 0:
        TestNumber += 1
        continue
    DivisibleBy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20]
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