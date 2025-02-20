#https://www.acmicpc.net/problem/2631
import sys, heapq
N = int(sys.stdin.readline().strip())
task = []
result = 0

for i in range(N):
    data = list(map(int,sys.stdin.readline().strip().split()))
    if data[0]+i < N:
        task.append([data[0]+i,data[1]])

for work in task:
    result += max(work)
        
print(result)