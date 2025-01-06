import sys
sys.setrecursionlimit(10**6)

def bfs(x,y,board,visited):
    global X, Y, people
    Q = []
    Q.append([x,y])
    direction = [(-1,0),(1,0),(0,-1),(0,1)]

    while Q:
        x,y = Q.pop()
        for dx, dy in direction:
            if x + dx >= 0 and x + dx < X and y + dy >= 0 and y + dy < Y and board[x+dx][y+dy] != 'X' and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                Q.append([x+dx,y+dy])
                if board[x+dx][y+dy] == "P":
                    people += 1
    return

X, Y = map(int,input().split())
board = [sys.stdin.readline().strip() for _ in range(X)]
visited = [[False]*Y for _ in range(X)]
people = 0

for i in range(X):
    for j in range(Y):
        if board[i][j] =='I':
            visited[i][j] = True
            bfs(i,j,board,visited)
            break
if people > 0:
    print(people)
else:
    print("TT")