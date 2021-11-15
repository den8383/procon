import sys
import collections

N, M = list(map(int, input().split()))

switches = list()
for i in range(M):
    switch = (list(map(int, input().split())))
    switches.append(switch[1:])

p = list(map(int, input().split()))

#print(N, M)
#print(switches)
#print(p)
#
#print()
cnt = 0
for bit in range(1 << N):
    ok = True
    bit = list(format(bit,'b').zfill(N))
    for m in range(M):
        sm = 0
        for s in switches[m]:
            sm = sm + int(bit[s - 1])
        if sm % 2 != p[m]:
            ok = False
            break
    if ok == True:
        cnt = cnt + 1
print(cnt)
