import heapq

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
maxDay = max(i[0] for i in arr)
tasks = [[] for _ in range(maxDay+1)]
result=0

for i, j in arr:
    tasks[i].append(j)

heap = []
for i in range(maxDay,0,-1):
    for j in tasks[i]:
        heapq.heappush(heap,-j)
    if heap:
        result-=heapq.heappop(heap)
print(result)