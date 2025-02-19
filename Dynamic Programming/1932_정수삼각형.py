#https://www.acmicpc.net/problem/1932
import sys
N = int(sys.stdin.readline().strip())
triangle = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            #선행 두 값중 최댓값 선택
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
print(max(dp[N-1]))