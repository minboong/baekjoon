N,K=map(int,input().split())
arr=list(input())
count=0
for i in range(N):
    if arr[i]=="P":
        for j in range(max(0,i-K),min(N,i+K+1)):
            if arr[j]=='H':
                count+=1
                arr[j]="O"
                arr[i]="O"
                break
print(count)
