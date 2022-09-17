# https://projecteuler.net/problem=2

import os
os.system("cls")
FibonacciList = []
AdditionList = []

for x in range(1,3) :
    FibonacciList.append(x)
for x in range(1, 31) :
    FibonacciList.append(FibonacciList[x-1] + FibonacciList[x])
for x in range(len(FibonacciList)) :
    if FibonacciList[x]%2 == 0 :
        AdditionList.append(FibonacciList[x])
print(FibonacciList)
print("The sum of all even numbers in the Fibonacci Sequence up to", FibonacciList[-1], "is",sum(AdditionList))
