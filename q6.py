ls = [i for i in range(1, 50)]
print("list before swapping: ", str(ls))
i = 0
b = 1
while i + 1 < len(ls):
    ls[i] = ls[i+1]
    a = ls[i+1]
    i += 1
print("list after swapping: ", str(ls))
