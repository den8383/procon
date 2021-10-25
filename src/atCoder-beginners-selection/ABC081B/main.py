import sys
import collections

num = input()
lines = input().split()
lines = list(map(int,lines))

count = 0
flag = False

while True:
    tmp = list()
    for i in lines:
        if i % 2 == 0:
            tmp.append(i / 2)
        else:
            flag = True
    lines = tmp
    if flag == True:
        break
    else:
        count = count + 1

print(count)
