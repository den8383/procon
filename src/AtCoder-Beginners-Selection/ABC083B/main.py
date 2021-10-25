import sys
import collections

#num = input()
lines = input().split()
lines = list(map(int,lines))
N, A, B = lines

toal = 0
for n in range(N + 1):
    n_separately = list(map(int,str(n)))
    sum_each_digit = 0
    for i in n_separately:
        sum_each_digit = sum_each_digit + i
    if sum_each_digit >= A and sum_each_digit <= B:
        toal = toal + n 

print(toal)
