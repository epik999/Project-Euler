# https://projecteuler.net/problem=6
SeperatelySquare = []
for x in range(1, 101) :
    SeperatelySquare.append(x**2)
SeperatelySquare = sum(SeperatelySquare)
SquareTogether = ((100*101)/2)**2

print(SeperatelySquare, SquareTogether)
Difference = SquareTogether-SeperatelySquare
print(Difference)