#https://www.acmicpc.net/problem/1149
import sys
N = int(sys.stdin.readline().strip())
dp = []
for _ in range(N):
    dp.append(list(map(int,sys.stdin.readline().strip().split())))
for i in range(1,N):
    for j in range(3):
        dp[i][j] += min(dp[i-1][j-1],dp[i-1][j-2])
print(min(dp[N-1]))