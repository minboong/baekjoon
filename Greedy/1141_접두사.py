N = int(input())
arr = [input() for i in range(N)]
remove=0
arr.sort(key=lambda x : len(x))
for i in range(N):
    for j in range(i+1,N):
        if arr[j][:len(arr[i])] == arr[i]:
            remove+=1
            break
print(N-remove)

# N = int(input())
# arr = [input().strip() for _ in range(N)]

# # 문자열 길이로 정렬
# arr.sort()

# # 접두사가 아닌 문자열 개수 확인
# count = 0
# for i in range(N):
#     if i == N - 1 or not arr[i + 1].startswith(arr[i]):
#         count += 1

# print(count)
