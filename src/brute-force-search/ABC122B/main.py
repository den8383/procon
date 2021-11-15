import sys
import collections

lines = list(input())
#lines = list(map(int,lines))
charactors = ['A','C','G','T']
ans = 0
count = 0

for l in lines:
    for c in charactors:
        if l == c:
            count = count + 1
            break
        elif c == charactors[-1]:
            count = 0
    ans = max(count,ans)

print(ans)
