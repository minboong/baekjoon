import sys
from dataclasses import dataclass,field
from collections import deque

@dataclass
class Node:
    value: int = None
    Child: list = field(default_factory=list)

def addChild(target, current):
    if target.value > current.value:
        if target.Child:
            for childNode in target.Child:
                addChild(childNode,current)
        newNode = Node()
        newNode.value = current.value
        target.Child.append(newNode)

N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))

for i in range(N):
    temp = Node()
    temp.value = arr[i]
    arr[i] = temp

current = 0
topNode = []

for i in range(len(arr)):
    node = arr[i]
    if node.value <= current:
        continue
    topNode.append(node)
    for j in range(i,len(arr)):
        if arr[j].value < node.value:
            addChild(node,arr[j])
    current = node.value

Q = deque()
for node in topNode:
    temp = [node,0]
    Q.append(temp)

maxDepth = 0
while Q:
    data = Q.popleft()
    if data[0].Child:
        for childNode in data[0].Child:
            Q.append([childNode,data[1]+1])
    if data[1] > maxDepth:
        maxDepth = data[1]
print(maxDepth+1)


# n = int(input())
# num_list = list(map(int,input().split()))

# dp = [1] * n

# for i in range(n):
#     for j in range(0, i):
#         if num_list[i] < num_list[j] :
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))