import sys
import collections

lines = input().split()
A,B,C,X,Y = list(map(int,lines))

A_num = 0
B_num = 0
C_num = 0
price = list()

for Z in range(0, 2*max(X,Y)+1, 2):
    C_num = Z
    A_num = max(0, X - 1/2*C_num)
    B_num = max(0, Y - 1/2*C_num) 
    price.append(int(A * A_num + B * B_num + C * C_num))
price = sorted(price)


print(price[0])

#
#A_num = 0
#B_num = 0
#C_A_num = 0
#C_B_num = 0
#
#p_num = list()
#for i in range(X+1):
#    A_num = i
#    C_A_num = 2*(X - i)
#    if Y+1-C_A_num <= 0:
#        p_num.append([A_num, B_num, C_A_num + C_B_num])
#    for i in range(1,Y+1-C_A_num):
#        B_num = i
#        C_B_num = 2*(Y - i)
#        p_num.append([A_num, B_num, C_A_num + C_B_num])
#
#
#price = A * p_num[0][0] + B * p_num[0][1] + C * p_num[0][2]
#
#print(p_num)
#for p in p_num:
#    price = min(price, A * p[0] + B * p[1] + C * p[2])
#print(price)
