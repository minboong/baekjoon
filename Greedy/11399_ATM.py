length=int(input())
arr=input()
arr=arr.split()
for i in range(len(arr)):
    arr[i]=int(arr[i])
arr.sort()
result=0
num=0
for i in arr:
    num+=int(i)
    result+=num
print(result)