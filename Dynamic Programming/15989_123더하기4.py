#https://www.acmicpc.net/problem/15989
import sys
N = int(sys.stdin.readline().strip())
result = []
dp = [[0,0] for _ in range(100001)]
dp[1],dp[2],dp[3] = [1,0], [2,1], [3,1]
#dp 배열의 두 번째 값은, 1이 포함되지 않은 조합의 갯수

for i in range(4,10001):
    if i % 3 != 0:
        dp[i][0] = dp[i-1][0] + dp[i-2][1]
        dp[i][1] = dp[i-2][1]
    else:
        dp[i][0] = dp[i-1][0] + dp[i-2][1] + 1
        dp[i][1] = dp[i-2][1] + 1

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    result.append(str(dp[num][0]))

print("\n".join(result))


# import sys
# N = int(sys.stdin.readline().strip())
# dp = [[1 for _ in range(10001)] for __ in range(2)]
# result = []
# for i in range(2,10001):
#     dp[1][i] = dp[1][i-2] + dp[0][i]
# dp.append(dp[1])
# for i in range(3,10001):
#     dp[2][i] = dp[2][i-3] + dp[1][i]
# for _ in range(N):
#     num = int(sys.stdin.readline().strip())
#     result.append(str(dp[2][num]))
# print("\n".join(result))