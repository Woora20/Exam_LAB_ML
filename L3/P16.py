import math
x = float(input("x: "))
M = int(input("M: "))
s = 0
for n in range(0, M + 1):
    s += (x ** n) / math.factorial(n)

print("s = %.5f" % s)

# Output
# x: 1
# M: 10
# s = 2.71828