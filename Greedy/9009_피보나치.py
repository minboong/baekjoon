T = int(input())
N = [int(input()) for _ in range(T)]
fibo=[0,1]

for num in N:
    result = []
    sent=""
    i = 1
    while num > 0:
        if fibo[i] <= num:
            if i+1 >= len(fibo):
                fibo.append(fibo[i] + fibo[i-1])
                i+=1
            else:
                i+=1
        else:
            result.append(fibo[i-1])
            num-=fibo[i-1]
            i = 1
    print(" ".join(map(str, result[::-1])))