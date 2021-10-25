import sys
import collections

num = int(input())
#lines = input().split()
lines = list()
for i in range(num):
    lines.append(input())
lines = sorted(set(list(map(int,lines))), reverse=True)
print(len(lines))
