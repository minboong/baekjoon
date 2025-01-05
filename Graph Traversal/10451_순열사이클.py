import sys
sys.setrecursionlimit(10**6)

def dfs(V):
    global visited
    global destination
    if not visited[V-1]:
        visited[V-1] = True
        dfs(destination[V-1])
    

N = int(input())
result = []
for _ in range(N):
    cycle = 0
    leng = int(input())
    #start = list(range(1,int(input())+1))
    destination = list(map(int,sys.stdin.readline().strip().split()))
    visited = [False] * leng
    for i in range(1,leng+1):
        if not visited[i-1]:
            dfs(i)
            cycle += 1
    result.append(cycle)
for n in result:
    print(n)