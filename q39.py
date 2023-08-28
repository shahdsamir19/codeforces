x = int(input("Enter the  number: "))
y = int(input("Enter the second number: "))
z = 0
if x < y:
    for i in range(x, y + 1):
        z = z + i
elif y < x:
    for i in range(y, x + 1):
        z = z + i


print("the sum of numbers from the lowest to the highest number is: "+str(z))