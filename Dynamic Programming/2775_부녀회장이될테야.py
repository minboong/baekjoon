#https://www.acmicpc.net/problem/2775
import sys
N = int(sys.stdin.readline().strip())
dp = [[i for i in range(15)] for _ in range(15)]
for i in range(1,15):
    for j in range(1,15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
for i in range(N):
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    print(dp[n][k])