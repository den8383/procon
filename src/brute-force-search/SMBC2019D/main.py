import sys
import collections
import itertools 


num = int(input())
lines = list(input())
count = 0

for i in range(1000):
    v = list(str(i).zfill(3))
    p = 0
    for j in range(num):
        if lines[j] == v[p]:
            p = p + 1
        if p == 3:
            break

    if p == 3:
        count = count + 1

print(count)















#num = int(input())
#lines = list(input())
#count = 0
#pwd = list()
#
#
#
#
#for v in range(1000):
#    v = list(str(v).zfill(3))
#    for i  in range(num):
#        s = lines
#        if s[i] == v[0]:
#            s = s[i+1:]
#            for j in range(len(s)):
#                if s[j] == v[1]:
#                    s = s[j+1:]
#                    for k in range(len(s)):
#                        if s[k] == v[2]:
#                            pwd.append(''.join(v))
#                    break
#print(len(set(pwd)))



#num = int(input())
#lines = list(input())
##lines = list(map(int,lines))
#
#c = itertools.combinations(lines,3)
#c = list(set(c))
#print(len(c))
