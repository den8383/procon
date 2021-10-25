import sys
import collections

num = input()
lines = input().split()
lines = list(map(int,lines))
lines = sorted(lines, reverse=True)

alice = 0
bob = 0
count = 0
for l in lines:
    if count % 2 == 0:
        alice = alice + l
    else:
        bob = bob + l
    count = count + 1
print(alice - bob)


