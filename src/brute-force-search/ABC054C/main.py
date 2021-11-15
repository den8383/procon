import sys
import collections
import itertools

N,M = list(map(int, input().split()))
graph = [[0]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
#print(graph)
#print(list(itertools.permutations(range(N))))
count = 0
for num in itertools.permutations(range(N)):
    ok = True
    if num[0] == 0:
        for i in range(N - 1):
            if graph[num[i]][num[i+1]] != 1:
                ok = False
        if ok == True:
            count = count + 1
print(count)
