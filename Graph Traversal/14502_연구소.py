import sys
from collections import deque

def bfs(x,y,board,visited,direction,N,M):
    #바이러스 감염 시작
    if not visited[x][y]:
        visited[x][y] = True
        Q = deque([[x,y]])
        while Q:
            temp = Q.popleft()
            x = temp[0]
            y = temp[1]
            for dx, dy in direction:
                if x + dx >= 0 and x + dx < N and y + dy >= 0 and y + dy < M and not visited[x+dx][y+dy] and board[x+dx][y+dy] == '0':
                    visited[x+dx][y+dy] = True
                    board[x+dx][y+dy] = '2'
                    Q.append((x+dx,y+dy))

N, M = map(int,input().split())
board_OG = [sys.stdin.readline().strip().split() for _ in range(N)]

result = 0
empty = []
virus = []
direction = [(-1,0),(1,0),(0,-1),(0,1)]

for n in range(N):
    for m in range(M):
        if board_OG[n][m] == '0':
            empty.append((n,m))
        elif board_OG[n][m] == '2':
            virus.append((n,m))

#빈 공간(0)이 N개 있으면, 그 중 3개를 골라 막음([1,2,3]번째, [1,2,4]번째... [n-2,n-1,n]번째)
for a in range(0,len(empty)-2):
    for b in range(a+1,len(empty)-1):
        for c in range(b+1,len(empty)):
            #reset board
            board = []
            for L in board_OG:
                temp=[]
                for i in L:
                    temp.append(i)
                board.append(temp)
            visited = [[False] * M for _ in range(N)]
            clear = 0

            board[empty[a][0]][empty[a][1]] = '1'
            board[empty[b][0]][empty[b][1]] = '1'
            board[empty[c][0]][empty[c][1]] = '1'
            for x,y in virus:
                bfs(x,y,board,visited,direction,N,M)
            #감염 후 남은 빈 공간 개수
            for n in range(N):
                for m in range(M):
                    if board[n][m] == "0":
                        clear +=1
            if clear > result:
                result = 0
                result += clear

print(result)