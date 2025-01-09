import sys
from collections import deque

def bfs(T,x,y,direction,visited,board,N):
    Q = deque([[x,y]])
    visited[x][y] = True
    while Q:
        x,y = Q.popleft()
        for dx, dy in direction:
            if x + dx >= 0 and x + dx < N and y + dy >= 0 and y + dy < N and not visited[x+dx][y+dy] and board[x+dx][y+dy] == T:
                visited[x+dx][y+dy] = True
                Q.append([x+dx,y+dy])

def countRegion(board,N):
    count = 0
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False] * N for _ in range(N)]

    for n in range(N):
        for m in range(N):
            if not visited[n][m]:
                target = board[n][m]
                bfs(target,n,m,direction,visited,board,N)
                count += 1
    return count


N = int(input())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

#계산
print(countRegion(board,N), end=" ")

#적록색약 보드 생성
for i in range(N):
    board[i] = list("".join(board[i]).replace('R','G'))

#계산
print(countRegion(board,N))