# https://projecteuler.net/problem=1

Numbers = []
NumberSum = 0
for x in range(1,1000) :
  if x%3 == 0 or x%5 == 0:
    Numbers.append(x)
print("The sum of all mutiples of 3 or 5 up to 1000 is",sum(Numbers))