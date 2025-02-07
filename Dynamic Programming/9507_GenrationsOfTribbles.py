def kng(n):
    global fibo
    result = 0
    if fibo[n]:
        return fibo[n]
    elif n<2:
        result = 1
    elif n == 2:
        result = 2
    elif n == 3:
        result = 4
    else:
        result = kng(n-1) + kng(n-2) + kng(n-3) + kng(n-4)
    fibo[n] = result
    return result

t = int(input())
fibo = [False for _ in range(68)]
answer=[]
for _ in range(t):
    n = int(input())
    answer.append(kng(n))
for num in answer:
    print(num)

