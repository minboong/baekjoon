N = int(input())

a = N//3
b = N%3

if a % 2 == 0:
    if b % 2 == 0:
        print("SK")
    else:
        print("CY")
else:
    if b % 2 == 0:
        print("CY")
    else:
        print("SK")

#print("CY" if N%2 else "SK")