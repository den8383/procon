import sys
import collections

num = input()
lines = input().split()
s = input()

a = int(num)
lines = list(map(int,lines))
b,c = lines

print(a + b + c, s)
