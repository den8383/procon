import sys
import collections

num = int(input())
lines = list()
for l in range(num):
    lines.append(list(map(int, input().split())))
#lines = list(map(int,lines))
ans = ''
t,x,y = 0,0,0
for line in lines:
    d_t = line[0] - t
    od_flag = (d_t) % 2
    d_x = line[1] - x
    d_y = line[2] - y
    sum_diff = d_x + d_y
    #print(sum_diff)
    #print('od_flag',od_flag == (abs(sum_diff)%2))
    #print('ABS',abs(d_x)+abs(d_y) <= d_t)
    if od_flag == (abs(sum_diff)%2) and abs(d_x)+abs(d_y) <= d_t:
        ans = 'Yes'
    else:
        ans = 'No'
        break

    t,x,y = line[0],line[1],line[2]

print(ans)
