def dfs(i, j, num, board, result):
    num += board[i][j]
    if len(num) == 6:
        if num not in result:
            result.append(num)
    else:
        if i+1 <= 4:
            dfs(i+1, j, num, board, result)
        if j+1 <= 4:
            dfs(i, j+1, num, board, result)
        if i-1 >= 0:
            dfs(i-1, j, num, board, result)
        if j-1 >= 0:
            dfs(i, j-1, num, board, result)


board = []
result=[]
for _ in range(5):
    board.append(input().split())
for i in range(5):
    for j in range(5):
        dfs(i,j,"",board,result)
print(len(result))