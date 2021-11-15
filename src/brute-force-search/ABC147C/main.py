import sys
import collections

N = int(input())

edc = [list() for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        edc[i].append([x - 1,y])


max_num = 0

for i in range(1 << N):
    i = list(map(int,format(i,'b').zfill(N)))
    ok = True
    for j in range(N):
        if i[j] == 1:
            for one_edc in edc[j]:
                if i[one_edc[0]] == one_edc[1]:
                    pass
                else:
                    ok = False
    if ok == True:
        max_num = max(max_num,sum(i))
    else:
        pass

print(max_num)




#def reverse_zero_one(s):
#    if s == 0:
#        return 1
#    elif s == 1:
#        return 0
#
#num = int(input())
##lines = list(map(int,lines))
#A = list()
#x = list()
#for _ in range(num):
#    A_num = int(input())
#    A.append(A_num)
#    x_num = list()
#    for _ in range(A_num):
#        x_num.append(list(map(int,input().split())))
#    x.append(x_num)
##print()
##print(A)
##print(x)
##
##print(x)
##print()
#
#for x_num in x:
#    j = [list() for _ in range(num)]
#    for x_i in x_num:
#        for s in x[x_i[0] - 1]:
#            print('s',s)
#            #print(s[1])
#            #print(j[s[0] - 1])
#            if j[s[0] - 1] != reverse_zero_one(s[1]) and j[s[0] - 1] != 'crn':
#                j[s[0] - 1] = s[1]
#            else:
#                j[s[0] - 1] = 'crn'
#            print(j)
