import sys
input = sys.stdin.readline
class QUEUE:
    def __init__(self):
        self.queue = [0]*50000
        self.front = 0
        self.rear = 0
    def push(self,item):
        self.front += 1
        self.queue[self.front] = item

    def pop(self):
        self.rear += 1
        return self.queue[self.rear]

N,M = map(int,input().split())
table = [input().rstrip() for _ in range(N)]

for i in range(N):
    table[i] = '0'+table[i]+'0'

table.insert(0,'0'*(M+2))
table.append('0'*(M+2))

visited = [0 for _ in range(N+2)]
visited[1] = visited[1]|1<<1

que = QUEUE()
que.push([1,1,1]) # r좌표,c좌표,cnt
direction = {0:[0,1] , 1:[0,-1] , 2:[1,0] , 3:[-1,0]}
while True :
    r,c,cnt = que.pop()
    if r == N and c == M:
        print(cnt)
        break

    for d in range(4):
        dr = r+direction[d][0]
        dc = c+direction[d][1]
        if visited[dr]&(1<<dc) or table[dr][dc] == '0':
            continue
        visited[dr] = visited[dr]|(1<<dc)
        que.push([dr,dc,cnt+1])