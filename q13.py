x = int(input("Please enter an integer: "))
print("The factors of ", str(x), "are: ")
for i in range(1, x+1):
    if x % i == 0:
        print(i)
