fruit, snake=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
for i in arr:
    if i <= snake:
        snake+=1
print(snake)
