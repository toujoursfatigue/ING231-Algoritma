import math
sonsuz= 1000000
n= 1
pi=0
while n < sonsuz:
    pi += 6/n**2
    n += 1
print(math.sqrt(pi))
