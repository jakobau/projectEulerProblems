# problem 4
# Largest Palindrome product
#
# 2.15.2020

# product of two 3-digit numbers

palindrome = []

for a in range(1, 999) :
    for b in range(1, 999) :
        mul = a*b
        mul = str(mul)
        mul = mul[len(mul)::-1]
        if int(mul)==(a*b) :
            palindrome.append(a*b)
palindrome.sort()
print(palindrome[len(palindrome)-1])
