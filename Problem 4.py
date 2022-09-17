# https://projecteuler.net/problem=4

PalindromicNumbers = []
Finsihed = False
for x in range(100, 1000) :
    for y in range(100,1000) :
        CurrentProduct = x*y
        if str(CurrentProduct) == str(CurrentProduct)[::-1] :
            PalindromicNumbers.append(CurrentProduct)

print("the largest palindromic number made from the product of 2 3-digit Numbers is", sorted(PalindromicNumbers)[-1])