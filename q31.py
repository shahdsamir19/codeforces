x = int(input("enter first num: "))
y = int(input("enter second num: "))
z = int(input("enter third num: "))
if x+y == z:
    print(str(x) + "+"+str(y)+"="+str(z))
if x*y == z:
    print(str(x) + "*"+str(y) + "=" + str(z))
if x**y == z:
    print(str(x) + "**"+str(y)+"="+str(z))
if y**x == z:
    print(str(y) + "**" + str(x)+"="+str(z))
if x-y == z:
    print(str(x) + "-" + str(y)+"="+str(z))
if y-x == z:
    print(str(y) + "-"+str(x)+"="+str(z))
if x/y == z:
    print(str(x) + "/"+str(y)+"="+str(z))
if y/x == z:
    print(str(y) + "/"+str(x)+"="+str(z))
if x % y == z:
    print(str(x), "%", str(y), "=", str(z))
if y % x == z:
    print(str(y), "%", str(x), "=", str(z))
