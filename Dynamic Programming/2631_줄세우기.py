#https://www.acmicpc.net/problem/2631
import sys
N = int(sys.stdin.readline().strip())
order = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp= [1 for _ in range(N)]

for i in range(N):
    current = order[i]
    for j in range(i+1,N):
        compare = order[j]
        if current < compare:
            if dp[i]+1 > dp[j]:
                dp[j] = dp[i]+1
print(N-max(weight))