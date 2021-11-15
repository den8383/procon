import sys
import collections

num = int(input())

divisors_s = list()
divisors_l = list()

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        divisors_s.append(i)
        divisors_l.insert(0, int(num/i))

divisors = divisors_s + divisors_l 
center_index = int(len(divisors)/2)
ans = max(len(str(divisors[center_index - 1])) ,len(str(divisors[-center_index])))
print(ans)










#
#num = int(input())
#
#divisors = list()
#
#for i in range(1,num + 1):
#    if num % i == 0:
#        divisors.append(i)
#center_index = int(len(divisors)/2)
#
##print(len(str(divisors[center_index - 1])) , len(str(divisors[-center_index])))
#ans = max(len(str(divisors[center_index - 1])) ,len(str(divisors[-center_index])))
#print(ans)
#
