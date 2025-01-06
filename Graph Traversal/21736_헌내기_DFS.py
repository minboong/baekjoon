import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,board,direction,visited):
    global X, Y
    global people
    if x < 0 or x >= X or y < 0 or y >= Y or board[x][y] == 'X':
        return
    if not visited[x][y]:
        visited[x][y] = True
        if board[x][y] == 'P':
            people+=1
        for dx, dy in direction:
            dfs(x+dx,y+dy,board,direction,visited)

X, Y = map(int,input().split())
board = [sys.stdin.readline().strip() for _ in range(X)]
visited = [[False]*Y for _ in range(X)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]
people = 0

for i in range(X):
    for j in range(Y):
        if board[i][j] =='I':
            dfs(i,j,board,direction,visited)
if people > 0:
    print(people)
else:
    print("TT")