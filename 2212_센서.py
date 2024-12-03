N=int(input())
K=int(input())-1
arr = list(map(int,input().split()))
arr.sort()
distance=[]
for i in range(len(arr)-1):
    distance.append(arr[i+1]-arr[i])
distance.sort(reverse=True)
print(sum(distance[K:]))