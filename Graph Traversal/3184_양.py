import sys
sys.setrecursionlimit(10**6)

def dfs(board,visited,x,y,end,cage):
    if visited[x][y] == 0:
        visited[x][y] = 1
        if board[x][y] == '#':
            return cage
        elif x == 0 or x == end[0] or y == 0 or y == end[1]:
            if x+1 <= end[0] and visited[x+1][y] != 1:
                dfs(board,visited,x+1,y,end,cage)
            if y+1 <= end[1] and visited[x][y+1] != 1:
                dfs(board,visited,x,y+1,end,cage)
            if x-1 >= 0 and visited[x-1][y] != 1:
                dfs(board,visited,x-1,y,end,cage)
            if y-1 >= 0 and visited[x][y-1] != 1:
                dfs(board,visited,x,y-1,end,cage)
            return []
        else:
            if board[x][y] == 'o' or board[x][y] == 'v':
                cage.append(board[x][y])
            if visited[x+1][y] == 0:
                dfs(board,visited,x+1,y,end,cage)
            if visited[x][y+1] == 0:
                dfs(board,visited,x,y+1,end,cage)
            if visited[x-1][y] == 0:
                dfs(board,visited,x-1,y,end,cage)
            if visited[x][y-1] == 0:
                dfs(board,visited,x,y-1,end,cage)
            return cage

x, y = map(int,sys.stdin.readline().split())
sheep = 0
wolf = 0
result_sheep = 0
result_wolf = 0
board=[]
end=[x-1,y-1]
cage = []
visited=[[0 for i in range(y)] for j in range(x)]
for _ in range(x):
    board.append(sys.stdin.readline())
board = [line.rstrip('\n') for line in board]
for i in range(0,x):
    for j in range(0,y):
        if(visited[i][j] != 1):
            cage = dfs(board,visited,i,j,end,cage)
        if cage:
            for a in cage:
                if a == "o":
                    sheep +=1
                else:
                    wolf +=1
            if sheep > wolf:
                result_sheep += sheep
            else:
                result_wolf += wolf
            sheep = 0
            wolf = 0

            cage = []
print(result_sheep, result_wolf)


# import sys
# sys.setrecursionlimit(10**6)

# def dfs(board,visited,x,y):
#     global sheep, wolf
#     global result
#     if x < 0 or x >= R or y < 0 or y >= C or board[x][y] == '#' or visited[x][y]:
#         return
#     visited[x][y]=True
#     if board[x][y] == 'v':
#         wolf += 1
#     elif board[x][y] == 'o':
#         sheep += 1
#     for dx, dy in directions:
#         dfs(board,visited,x + dx,y + dy)

# R, C = map(int,sys.stdin.readline().split())
# #R 세로 C 가로
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]
# visited = [[False] * C for _ in range(R)]
# sheep = 0
# wolf = 0
# result=[0,0]

# directions = [(0,-1), (0,1), (-1,0), (1, 0)]


# for x in range(R):
#     for y in range(C):
#         if visited[x][y] == False and board[x][y] != '#':
#             dfs(board,visited,x,y)
#             if sheep > wolf:
#                 result[0] += sheep
#             else:
#                 result[1] += wolf
#             sheep = 0
#             wolf = 0


# print(result[0], result[1])