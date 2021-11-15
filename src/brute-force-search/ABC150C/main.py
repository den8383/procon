import sys
import collections
import itertools

num = int(input())
lines = list()
for _ in range(2):
    lines.append(list(map(int,(input().split()))))
#lines = list(map(int,lines))

lines = sorted(lines)


sequence = list(range(1, num + 1))
sequence = list(map(list,list(itertools.permutations(sequence,num))))
print(abs(sequence.index(lines[0]) - sequence.index(lines[1])))
