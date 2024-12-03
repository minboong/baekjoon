N, K = map(int,input().split())
arr= [int(input()) for _ in range(N)]
#arr=[]
# for i in range(N):
#     arr.append(int(input()))
arr.reverse()
count=0
i=0
while K > 0:
    if arr[i] <= K:
        count += K//arr[i]
        K %= arr[i]
    if arr[i] > K:
        i+=1
print(count)