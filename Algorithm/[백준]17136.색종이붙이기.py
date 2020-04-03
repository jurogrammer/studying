def Check(table,r,c,n):
    for i in range(r,r+n):
        for j in range(c,c+n):
            if i<0 or j<0 or i>=10 or j >=10 or table[i][j] == 0:
                return False

    return True

def Apply(table,r,c,n):
    for i in range(r,r+n):
        for j in range(c,c+n):
            table[i][j] = 0

def Eraise(table,r,c,n):
    for i in range(r, r + n):
        for j in range(c, c + n):
            table[i][j] = 1

minVal = 101
def DFS(r,c,cnt):
    global minVal
    if cnt>minVal:
        return

    if r >= 10:
        minVal = min(minVal,cnt)
        return

    if c >= 10:
        DFS(r+1,0,cnt)
        return

    if table[r][c] != 1:
        DFS(r,c+1,cnt)
        return

    for n in range(5,0,-1):
        if remains[n] <= 0:
            continue
        if not Check(table,r,c,n):
            continue
        Apply(table,r,c,n)
        remains[n]-=1
        DFS(r,c+n,cnt+1)
        Eraise(table,r,c,n)
        remains[n]+=1

#oneList 생성하기
table = [list(map(int,input().split())) for _ in range(10)]
total = 0
for i in range(10):
    total += sum(table[i])
if total == 0:
    print(0)
else:#돌리기
    remains = [0,5,5,5,5,5]
    DFS(0,0,0)
    if minVal == 101:
        minVal = -1
    print(minVal)