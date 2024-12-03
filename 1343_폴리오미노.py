arr=list(input().split('.'))
result=""
for let in arr:
    l=len(let)
    if l >= 4:
        result += "AAAA" * (l//4)
        l = l%4
    if l >= 2:
        result += "BB" * (l//2)
        l = l%2
    if l != 0:
        result = '-1'
        break
    result += '.'
if result[-1]==".":
    result = result[:-1]
print(result)