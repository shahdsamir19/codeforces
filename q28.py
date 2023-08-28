num = int(input("input a four digit numbers: "))

x = num//1000

x1 = (num-x*1000)//100

x2 = (num-x*1000-x1*100)//10

x3 = num-x*1000-x1*100-x2*10

print("the sum of digits in the number is", x+x1+x2+x3)

if x**3+x1**3+x2**3+x3**3 == num:
    print("the number is armstrong")
    