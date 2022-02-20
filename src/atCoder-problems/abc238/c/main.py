import sys
import collections
import itertools

num = int(input())

#print(len(str(num)))
digitnum = len(str(num))
total = 0
n = 0
for i in range(1,digitnum):
    n = 9*10**(i - 1)
    total += (n * (n + 1))//2

n = num - (10**(digitnum - 1) - 1)
total += (n * (n + 1))//2
print(int(total % 998244353))

