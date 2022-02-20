import sys
import collections
import itertools

num = int(input())
if 2**num > num**2:
    print('Yes')
else:
    print('No')
