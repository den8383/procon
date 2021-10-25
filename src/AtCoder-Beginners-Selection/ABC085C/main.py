import sys
import collections

#num = input()
lines = input().split()
lines = list(map(int,lines))
N,Y = lines
flag = False

for x in range(N+1):
    for y in range(N+1-x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            flag = True
            break
    if flag == True:
        break
                
if flag == False:
    x,y,z = -1, -1, -1
    
                

print(x,y,z)
