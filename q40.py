def fibonacci(size):

    a = 1

    b = 1

    i = 0

    while i < size:

        print(a)

        a, b = b, a+b

        i += 1


n = int(input("enter a size : "))
print(fibonacci(n))
