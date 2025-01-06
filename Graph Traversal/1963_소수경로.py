import sys, math
from collections import deque

def bfs(start,end):
    Q = deque()
    visited = [False]*10000
    Q.append([start,0])
    visited[start] = True
    while Q:
        num = Q.popleft()
        for i in range(4):
            for j in range(10):
                current = list(str(num[0]))
                current[i] = str(j)
                if current[0] != '0' and int("".join(current)) != num[0]:
                    if int("".join(current)) == end:
                        return num[1] + 1
                    if not visited[int("".join(current))] and Pnum[int("".join(current))]:
                        Q.append([int("".join(current)),num[1]+1])
                        visited[int("".join(current))] = True
    return "Impossible"
    
def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

N = int(input())
Pnum = []
Pnum = [False]*10000
for i in range(1000,10000):
    if isPrime(i):
        Pnum[i]=True

result = []
for _ in range(N):
    start, end = map(int,sys.stdin.readline().strip().split())
    if start == end:
        result.append(0)
    else:
        result.append(bfs(start,end))
for i in result:
    print(i)