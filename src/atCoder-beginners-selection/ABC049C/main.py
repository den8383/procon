import sys
import collections
import re

S = input()
#lines = input().split()
#lines = list(map(int,lines))
#print(num)
#print(lines)
#print(S)
if len(S) == 0:
    print('NO')
    sys.exit()
words = ['dream','dreamer','erase','eraser']

while True:
    for word in words:
        if S[-len(word):] == word:
            S = S[:-len(word)]
            if len(S) == 0:
                print('YES')
                sys.exit()
            break
        elif word == words[-1]:
            print('NO')
            sys.exit()


#S = ''.join(reversed(S))
#dream = ''.join(reversed('dream'))
#dreamer = ''.join(reversed('dreamer'))
#erase = ''.join(reversed('erase'))
#eraser = ''.join(reversed('eraser'))
#while len(S) != 0:
#    serached =re.search(dream+'|'+dreamer+'|'+erase+'|'+eraser,S)
#    #print(serached)
#    #print(type(serached))
#    if serached is None:
#        break
#    elif serached.start() != 0:
#        break
#    S = S[serached.end():]
#    #print(S)
#
#if len(S) != 0:
#    print('No')
#else:
#    print('YES')
