import sys

input = sys.stdin.readline

def rotate(table,parameters):
    r,c,s = parameters

    for n in range(1,s+1):
        y1 = r+n
        y2 = r-n
        x1 = c+n
        x2 =
        temp = table[r+n][c-n]
        for dc in range(2*n):
            table[r+n][c-n+dc] = table[r+n][c-n+(dc+1)]

        for dr in range(2 * n):
            table[r+n-dr][c+n] = table[r+n-(dr+1)][c+n]

        for dc in range(2*n):
            table[r-n][c+n-dc] = table[r-n][c+n-(dc+1)]

        for dr in range(2*n-1):
            table[r-n + dr][c-n] = table[r-n + (dr+1)][c-n]
        table[r+n-1][c-n] = temp
    return table

def getMinVal(table):
    global n
    val = 99999999
    for i in range(n):
        val = min(val,sum(table[i]))
    return val

def DFS(table,i,visited):
    global minVal
    global rotateList
    global n
    global k

    if i == k :
        tempVal = getMinVal(table)
        if minVal > tempVal:
            minVal = tempVal
        return

    for x in range(k):
        if not visited&(1<<x):
            rotatedTable = rotate([table[i][:] for i in range(n)],rotateList[x])
            DFS([rotatedTable[i][:] for i in range(n)],i+1,visited|(1<<x))


n,m,k = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]
rotateList = [] #변환 필요 1씩 빼야 함.! 1,1부터 시작.

for _ in range(k):
    r,c,s = map(int,input().split())
    rotateList.append((r-1,c-1,s))

minVal = 999999
DFS(table,0,0)

print(minVal)