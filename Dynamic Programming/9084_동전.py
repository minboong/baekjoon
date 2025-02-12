#https://www.acmicpc.net/problem/9084
#https://d-cron.tistory.com/23
import sys

T = int(sys.stdin.readline().strip())
result = []

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coin = list(map(int,sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    
    dp = []
    for i in range(N):
        if i > 0:
            dp.append(dp[i-1])
        else:
            dp.append([0] * (M+1))
            dp[i][0] = 1
        for j in range(coin[i],M+1):
                dp[i][j] += dp[i][j-coin[i]]
    result.append(str(dp[-1][-1]))

print("\n".join(result))