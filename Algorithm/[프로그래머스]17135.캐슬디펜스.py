from collections import deque

def GetArchers(M):
    archers = []
    for i in range(M):
        for j in range(i+1,M):
            for k in range(j+1,M):
                archers.append([i,j,k])
    return archers

def attackPlace(table,N,M,D,archer):
    ac = archer
    dq = deque([])
    dq.appendleft((N-1,ac))
    for d in range(1,D+1):
        size = len(dq)
        for _ in range(size):
            r,c = dq.popleft()
            if r<0 or c<0 or c>=M:
                continue
            if table[r][c] == 1:
                return (r,c)
            else:
                dq.append((r-1,c))
        dq.appendleft((N-1,ac-d))
        dq.append((N-1,ac+d))
    return (-1,-1)

def GoDownAnermy(table):
    for r in range(N-1,0,-1):
        for c in range(M):
            table[r][c] = table[r-1][c]

    for c in range(M):
        table[0][c] = 0

N,M,D = map(int,input().split())
originTable = [list(map(int,input().split())) for _ in range(N)]

archerList = GetArchers(M)
rst = 0
#모든 archer의 경우에 대해서,
for archers in archerList:
    table = [originTable[i][:] for i in range(N)]
    val = 0
    #M턴 반복
    for _ in range(N+1):
        #궁수가 죽일 수 있는 적 찾기
        anermys = set()
        for archer in archers:
            r,c = attackPlace(table,N,M,D,archer)
            if r==-1 and c==-1:
                continue
            else:
                anermys.add((r,c))
        #죽인 적 수 추가
        val += len(anermys)
        for r,c in anermys:
            table[r][c] = 0
        #궁수가 죽인 후 적 한칸 내려옴.
        GoDownAnermy(table)

    #최대 적의 수인지 파악
    if val>rst:
        rst = val

print(rst)