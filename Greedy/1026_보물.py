def findMax(arr):
    maxNum=0
    maxI=0
    for i in range(len(arr)):
        if arr[i] > maxNum:
            maxNum = arr[i]
            maxI = i
    return maxI

N=int(input())
A2=[0]*N
#B2=[0]*N
A=input().split()
B=input().split()
for i in range(N):
    A[i]=int(A[i])
    B[i]=int(B[i])
A1=[]
B1=[]
for i in B:
    B1.append(i)
for i in A:
    A1.append(i)
A1.sort()
rank=1
for i in range(N):
    if rank>N:
        break
    num = findMax(B1)
    B1[num]=0
    A2[num]=A1[rank-1]
    rank+=1
result=0
i=0
while i<N:
    result+=A2[i]*B[i]
    i+=1
print(result)

# # 입력 받기
# n = int(input())  # 배열의 크기
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# # 정렬
# A.sort()  # A는 오름차순
# B.sort(reverse=True)  # B는 내림차순

# # 최소 합 계산
# result = sum(a * b for a, b in zip(A, B))

# # 결과 출력
# print(result)

