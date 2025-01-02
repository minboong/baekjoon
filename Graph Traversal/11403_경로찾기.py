import sys
from collections import deque

def bfs(V, N, G):
    result=[]
    visited = [False] * (N+1)
    q = deque()
    q.append(V)
    while q:
        num = q.popleft()
        for i in range(1,N+1):
            if G[num-1][i-1] == '1' and not visited[i]:
                visited[i] = True
                q.append(i)
    for i in range(N):
        if visited[i+1]:
            result.append('1')
        else:
            result.append('0')
    return result

N = int(sys.stdin.readline().rstrip())
G = [sys.stdin.readline().rstrip().split() for _ in range(N)]
for i in range(1,N+1):
    result = bfs(i, N, G)
    print(" ".join(result))