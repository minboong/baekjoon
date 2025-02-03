import sys
N = int(input())
p = list(map(int,sys.stdin.readline().strip().split()))
P = [0]
for i in p:
    P.append(i)

dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for k in range(i+1):
        dp[i] = max(dp[i],dp[i-k]+P[k])
print(dp[N])

#dp N 은 
#dp[N-1] + P[1], dp[N-2] + P[2], dp[N-3] + P[3] ... 중 가장 큰 값