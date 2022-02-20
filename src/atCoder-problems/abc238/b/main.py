import sys
import collections
import itertools

num = int(input())
lines = input().split()
lines = list(map(int,lines))
slash_list = list()
slash_list.append(0)
angle = 0
for line in lines:
    angle += line
    slash_list.append(angle%360)
slash_list = sorted(slash_list)
slash_list.append(360)

max_angle = 0
for i in range(len(slash_list) - 1):
    max_angle = max(max_angle,abs(slash_list[i] - slash_list[i+1]))


print(max_angle)
