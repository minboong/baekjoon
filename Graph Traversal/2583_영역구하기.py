import sys
from collections import deque

def bfs(x,y,board):
    N = len(board[0])
    M = len(board)
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    count = 1
    Q = deque([[x,y]])
    board[x][y] = True
    while Q:
        cx, cy = Q.popleft()
        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if nx < M and ny < N and nx >= 0 and ny >= 0:
                if not board[nx][ny]:
                    count += 1
                    Q.append([nx,ny])
                    board[nx][ny] = True
    return count

M, N, K = map(int,input().split())
rectangle = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(K)]
board = [[False] * N for _ in range(M)]
for x1, y1, x2, y2 in rectangle:
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[j][i] = True
result=[]
for i in range(M):
    for j in range(N):
        if not board[i][j]:
            result.append(bfs(i,j,board))
result.sort()
print(len(result))
print(" ".join(map(str,result)))