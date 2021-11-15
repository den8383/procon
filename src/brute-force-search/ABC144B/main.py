import sys
import collections

num = int(input())
ans = 'No'
for n in range(1, 10):
    if (num/n).is_integer() and num/n <= 9:
        ans = 'Yes'

print(ans)
