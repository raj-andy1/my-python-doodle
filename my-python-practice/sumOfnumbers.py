i = 1
n=2
totalOdd = 0
totalEven = 0
while i <= 2017:
    totalOdd += i
    i += 2

while n<=2016:
    totalEven += n
    n += 2

print(totalOdd)
print(totalEven)
print(totalOdd - totalEven)

