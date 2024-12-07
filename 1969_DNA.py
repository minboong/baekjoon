N, M = map(int,input().split())
dna=[]
result=[]
hd=0
for _ in range(N):
    dna.append(input())
for i in range(M):
    NCT=[0,0,0,0]
    for j in dna:
        if j[i]=='A':
            NCT[0]+=1
        elif j[i]=='C':
            NCT[1]+=1
        elif j[i]=='G':
            NCT[2]+=1
        else:
            NCT[3]+=1
    if NCT[0]==max(NCT):
        result.append('A')
        hd += (sum(NCT)-NCT[0])
    elif NCT[1]==max(NCT):
        result.append('C')
        hd += (sum(NCT)-NCT[1])
    elif NCT[2]==max(NCT):
        result.append('G')
        hd += (sum(NCT)-NCT[2])
    else:
        result.append('T')
        hd += (sum(NCT)-NCT[3])
for i in result:
    print(i,end="")
print()
print(hd)

# import sys

# # 입력 처리
# N, M = map(int, sys.stdin.readline().split())
# dna = [sys.stdin.readline().strip() for _ in range(N)]

# # 결과 변수
# result = []
# hdist = 0

# # 각 열에 대해 처리
# for col in range(M):
#     # A, C, G, T의 빈도 계산
#     counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
#     for row in dna:
#         counts[row[col]] += 1
    
#     # 가장 빈도 높은 문자 선택
#     max_char = max(counts, key=lambda x: (counts[x], -ord(x)))
#     result.append(max_char)
    
#     # 해밍 거리 계산
#     hdist += N - counts[max_char]

# # 결과 출력
# print("".join(result))
# print(hdist)