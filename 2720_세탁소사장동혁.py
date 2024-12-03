N=int(input())
money=[]
for i in range(N):
    money.append(int(input()))
for i in range(N):
    cash=money[i]
    print(cash//25,end=" ")
    cash%=25
    print(cash//10,end=" ")
    cash%=10
    print(cash//5,end=" ")
    cash%=5
    print(cash)