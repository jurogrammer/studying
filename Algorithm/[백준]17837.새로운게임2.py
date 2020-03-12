'''
https://jurogrammer.tistory.com/9
'''
import sys
input = sys.stdin.readline
direction = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]
class Horse:
    def __init__(self,r,c,d):
        self.r = r
        self.c = c
        self.d = d

def turnDirect(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    else:
        return 3

N,K = map(int,input().split())

#테이블 생성
table = [[[3,[],0] for _ in range(N+2)] for _ in range(N+2)] #벽 고려해서 생성

for r in range(1,N+1):
    colors = tuple(map(int,input().split()))
    for i in range(1,N+1):
        table[r][i][0] = colors[i-1]

horseList = []
for _ in range(K):
    r,c,d = map(int,input().split())
    h = Horse(r,c,d)
    horseList.append(h)
    table[r][c][1].append(h)
    table[r][c][2] += 1

t = 0
flag = False
while t<=1000:
    t += 1
    for i in range(K):
        h = horseList[i]
        nr,nc = h.r+direction[h.d][0] ,h.c+direction[h.d][1]

        if table[nr][nc][0] == 0:
            curHorse = table[h.r][h.c][1].pop()
            table[h.r][h.c][2] -= 1
            tempStack = [curHorse]

            while h != curHorse:
                curHorse = table[h.r][h.c][1].pop()
                tempStack.append(curHorse)
                table[h.r][h.c][2] -= 1

            while tempStack:
                moveHorse = tempStack.pop()
                moveHorse.r,moveHorse.c = nr,nc
                table[nr][nc][1].append(moveHorse)
                table[nr][nc][2] += 1

        elif table[nr][nc][0] == 1:
            curHorse = table[h.r][h.c][1].pop()
            table[nr][nc][1].append(curHorse)
            table[h.r][h.c][2] -= 1
            table[nr][nc][2] += 1
            curHorse.r,curHorse.c = nr,nc
            while h != curHorse:
                curHorse = table[h.r][h.c][1].pop()
                table[nr][nc][1].append(curHorse)
                table[h.r][h.c][2] -= 1
                table[nr][nc][2] += 1
                curHorse.r, curHorse.c = nr, nc

        else:
            # 방향 바꾸기
            h.d = turnDirect(h.d)
            nr,nc = h.r + direction[h.d][0],h.c +direction[h.d][1]

            if table[nr][nc][0] == 2 or table[nr][nc][0] == 3:
                pass
            else:
                if table[nr][nc][0] == 0:
                    curHorse = table[h.r][h.c][1].pop()
                    table[h.r][h.c][2] -= 1
                    tempStack = [curHorse]

                    while h != curHorse:
                        curHorse = table[h.r][h.c][1].pop()
                        tempStack.append(curHorse)
                        table[h.r][h.c][2] -= 1

                    while tempStack:
                        moveHorse = tempStack.pop()
                        moveHorse.r, moveHorse.c = nr, nc
                        table[nr][nc][1].append(moveHorse)
                        table[nr][nc][2] += 1

                elif table[nr][nc][0] == 1:
                    curHorse = table[h.r][h.c][1].pop()
                    table[nr][nc][1].append(curHorse)
                    table[h.r][h.c][2] -= 1
                    table[nr][nc][2] += 1
                    curHorse.r, curHorse.c = nr, nc
                    while h != curHorse:
                        curHorse = table[h.r][h.c][1].pop()
                        table[nr][nc][1].append(curHorse)
                        table[h.r][h.c][2] -= 1
                        table[nr][nc][2] += 1
                        curHorse.r, curHorse.c = nr, nc

        if table[h.r][h.c][2]>=4:
            flag = True
            break

    if flag:
        break


if flag:
    print(t)
else:
    print(-1)
