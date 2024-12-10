N, K = map(int,input().split())
H = list(map(int,input().split()))
cost = []
for i in range(N-1):
    cost.append(H[i+1]-H[i])
cost.sort(reverse=True)
result = 0
for i in cost[K-1:]:
    result+=i
print(result)