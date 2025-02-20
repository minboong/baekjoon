#https://www.acmicpc.net/problem/4811
result=[]
dp = [[0 for i in range(32)] for j in range(32)]
for i in range(1,32):
    for j in range(1,32):
        if i > j:
            dp[i][j] = 0
        elif i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if not n:
        break
    result.append(dp[n][n+1])
for answer in result:
    print(answer)