import sys
from collections import deque
import math



def bfs(location,destination,X,direction):
    if location[0] == destination[0] and location[1] == destination[1]:
        return 0
    visited = [[False] * X for _ in range(X)]
    cx, cy = location[0], location[1]
    visited[cx][cy] = True
    Q = deque([location])
    while Q:
        current = Q.popleft()
        cx, cy = current[0],current[1]
        temp = []
        for dx, dy in direction:
            nx, ny = current[0] + dx, current[1] + dy
            if nx >= 0 and nx < X and ny >= 0 and ny < X and not visited[nx][ny]:
                if [nx,ny] == destination:
                    return current[2]+1
                visited[nx][ny] = True
                Q.append([nx,ny,current[2]+1])

N = int(input())
direction = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

result =[]
for _ in range(N):
    X = int(input())
    location = list(map(int,input().split()))
    location.append(0)
    destination = list(map(int,input().split()))
    result.append(bfs(location,destination,X,direction))

for i in result:
    print(i)