base = int(input("enter the base: "))

exponent = int(input("enter the power: "))

result = 1

while exponent != 0:

    result *= base

    exponent -= 1

print("answer = "+str(result))
