from functools import lru_cache
@lru_cache(None)
def pascal(n,k):
    if k == 1:
        return 1
    if k == n:
        return 1
    return pascal(n-1,k-1) + pascal(n-1,k)

n, k = map(int,input().split())
print(pascal(n,k))

# n, k = map(int, input().split())

# dp = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             dp[i][j] = 1  # 파스칼 삼각형의 양쪽 끝은 항상 1
#         else:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

# print(dp[n][k])
