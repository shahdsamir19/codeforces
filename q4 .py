n = int(input("please enter number: "))
factorial = 1
i = 1
if n == 0 or n == 1:
    print("factorial = ", str(factorial))
else:
    while i < n:
        i = i + 1
        factorial = factorial * i
    print("factorial = ", str(factorial))
