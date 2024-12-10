import math

def combination(box):
    num_0 = 0
    total = 0
    a = 0
    b = 0
    for i in box:
        if i == 0:
            num_0 += 1
        total += i
        if a == 0:
            a += i
        else:
            b = i
        
    if num_0 == 2:
        return 1
    if num_0 == 1:
        return math.comb(total,a)
    else:
        return math.comb(total,a) * math.comb(total-a,b)

N = int(input())
arr = [int(input()) for _ in range(N)]

for num in arr:
    box = [0,0,0]
    result=0   
    box[2] = num // 3
    if num % 3 ==  1:
        box[0] += 1
    elif num % 3 == 2:
        box[1] += 1

    while box[1]!=0 or box[2]!=0:
        result += combination(box)
        if box[1] > 0:
            box[1] -= 1
            box[0] += 2
        elif box[2] > 0:
            box[2] -= 1
            box[1] = (num - box[2]*3) // 2
            box[0] = (num - box[2]*3) % 2
    print(result + 1)


# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


# def solve():
#     T = int(input())  # 테스트 케이스 개수
#     cases = [int(input()) for _ in range(T)]  # 각 테스트 케이스 입력
#     max_n = max(cases)  # 가장 큰 숫자를 기준으로 DP 배열 계산
    
#     # DP 배열 초기화
#     dp = [0] * (max_n + 1)
#     dp[1] = 1
#     if max_n > 1:
#         dp[2] = 2
#     if max_n > 2:
#         dp[3] = 4
    
#     # DP 계산
#     for i in range(4, max_n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
#     # 결과 출력
#     for n in cases:
#         print(dp[n])

# solve()
