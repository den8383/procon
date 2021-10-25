import sys
import collections

A = int(input())
B = int(input())
C = int(input())
D = int(input())
#lines = list(map(int,lines))

count = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            ans = a*500 + b*100 + 50*c
            if ans == D:
                count = count + 1
print(count)
