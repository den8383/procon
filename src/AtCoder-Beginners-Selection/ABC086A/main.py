import sys
import collections

#num = input()
lines = input().split()
lines = list(map(int,lines))
a,b = lines

if a*b%2 == 0:
    print('Even')
else:
    print('Odd')
