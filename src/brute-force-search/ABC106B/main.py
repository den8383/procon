import sys
import collections

num = int(input())
ans = 0

for i in range(1, num + 1):
    count = 0
    for n in range(1, i + 1):
        if n % 2 == 1 and i % n == 0:
            count = count + 1
    if count == 8:
        ans = ans + 1

print(ans)
