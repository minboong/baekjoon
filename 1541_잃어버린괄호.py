arr = input().split('-')
for i in range(len(arr)):
    if '+' in arr[i]:
        string = arr[i].split('+')
        temp = 0
        for num in string:
            temp+=int(num)
        arr[i]=temp
    else:
        arr[i]=int(arr[i])
result=int(arr[0])*2
for i in arr:
    result-=i
print(result)