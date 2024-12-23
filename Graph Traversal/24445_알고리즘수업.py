import sys

def bfs(V, E, R):
    queue = []
    od = 1
    queue.append(R)
    order[R] = od
    V[R] = 1
    while len(queue) != 0:
        u = queue.pop(0)
        for i in E[u]:
            if V[i] != 1:
                od +=1
                V[i] = 1
                queue.append(i)
                order[i] = od


v_num, e_num, R = map(int,sys.stdin.readline().split())
V = {}
for i in range(v_num+1):
    V[i+1] = 0
order = [0 for _ in range(v_num + 1)]
E = [[] for _ in range(v_num + 1)]
for _ in range(e_num):
    a, b = map(int,sys.stdin.readline().split())
    E[a].append(b)
    E[b].append(a)
for e in E:
    e.sort(reverse=True)
bfs(V, E, R)
for i in order[1:]:
    print(i)