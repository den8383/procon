import sys
import collections
import itertools

num = int(input())
lines = list()
for _ in range(num):
    lines.append(list(map(int,input().split())))
perm = list(itertools.permutations(lines,len(lines)))

total = 0
for p in perm:
    route = 0
    p = list(p)
    for i in range(len(p) - 1):
        route = route + ((p[i][0] - p[i+1][0])**2 + (p[i][1] - p[i+1][1])**2)**(1/2)
    total = total + route
print(total/len(perm))
