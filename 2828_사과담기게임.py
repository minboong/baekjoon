screen, basket = map(int,input().split())
b_left=0
b_right=b_left+basket-1
dis=0
N = int(input())
apple = [int(input()) for i in range(N)]
for a in apple:
    if a > b_right:
        move_dis = a - b_right
        dis += move_dis
        b_left += move_dis
        b_right += move_dis
    elif a < b_left:
        move_dis = b_left - a
        dis += move_dis
        b_right -= move_dis
        b_left -= move_dis
print(dis)