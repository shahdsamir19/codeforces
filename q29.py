x = int(input("please enter start value:"))

y = int(input("please enter end value: "))

nums = [i for i in range(x+1, y)if i % 9 == 0 and i % 4 != 0]

print(nums)
