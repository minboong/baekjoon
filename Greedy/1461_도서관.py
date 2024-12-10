n,m = map(int,input().split())
book = list(map(int, input().split()))
book.sort()
pos=[]
neg=[]
dis=0
for i in book:
    if i > 0:
        pos.append(i)
    else:
        neg.append(0-i)
        
pos.sort(reverse=True)
neg.sort(reverse=True)


#배열이 비었을 때 예외처리 포함
if pos and (not neg or pos[0] >= neg[0]) :
    last = pos[0]
elif neg:
    last = neg[0]

for i in range(0, len(neg), m):
    dis += 2 * neg[i]

for i in range(0, len(pos), m):
    dis += 2 * pos[i]
print(dis-last)
