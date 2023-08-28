def decimaltobinary(n):

    b_number = 0
    cnt = 0
    while n != 0:
        rem = n % 2
        c = pow(10, cnt)
        b_number += rem * c
        n //= 2
        cnt += 1
    return b_number


x = int(input("Enter a decimal num: "))

if x > 255 or x < 0:
    print("error")
else:
    print("it's binary equivalent: ")
    print(decimaltobinary(x))
