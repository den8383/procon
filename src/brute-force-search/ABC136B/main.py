import sys
import collections

num = int(input())
count = 0

for n in range(1, num+1):
    if len(str(n)) % 2 == 1:
        count = count + 1

print(count)
