string=input()
arr=[]
before=''
num=''
for i in string:
    if before == i:
        num+=i
    else:
        if num != '':
            arr.append(num)
        before = i
        num=i
if num != '':
    arr.append(num)
print(len(arr)//2)