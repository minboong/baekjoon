seat=int(input())
string=input().replace('LL','S')
if(len(string)+1>seat):
    print(seat)
else:
    print(len(string)+1)