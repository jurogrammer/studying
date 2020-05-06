dr = (0,0,-1,1)
dc = (-1,1,0,0)

def getCsdCells(table):
    csdCells = []
    keys = table.keys()
    for key in keys:
        state, ellaps,x = table[key]
        if state == 2 :
            continue
        else:
            csdCells.append([key,[state,ellaps,x]])
    return csdCells

#들어가는 원소는 모두 리스트.
def spread(r,c,x,table):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        #비어 있는 경우
        if (nr,nc) not in table:
            table[(nr,nc)] = [0,0,x]
        else:
            existCellAtt = table[(nr,nc)]
            existCellstate,existCellEllaps, existCellX = existCellAtt

            #있다면 방금 생성됬고, 생명력이 더 낮은 애라면 자리차지. 그 외는 아무것도 못함.
            if existCellstate == 0 and existCellEllaps == 0 and  x > existCellX:
                table[(nr,nc)] = [0,0,x]

def getRemainArriveCells(table):
    totalCells = 0
    keys = table.keys()
    for key in table.keys():
        state, ellaps, x = table[key]
        if state != 2:
            totalCells += 1

    return totalCells



testCase = int(input())

for test in range(1,testCase+1):
    n,m,k = map(int,input().split())

    inputTable = [list(map(int,input().split())) for _ in range(n)]

    table = {}
    for i in range(n):
        for j in range(m):
            if inputTable[i][j] == 0 :
                continue
            table[(i,j)] = [0,0,inputTable[i][j]] #상태, 상태경과시간, 생명력 //(r,c) ,(state,ellaps,x) = cells.popitem()

    #시간경과
    for _ in range(k):
        csdCells = getCsdCells(table)
        for position, att in csdCells:
            r,c = position
            state, ellaps, x = att

            #시간경과
            ellaps += 1

            #비활성
            if state == 0 :
                if ellaps == x :
                    state = 1
                    ellaps = 0

            #활성
            elif state == 1:
                if ellaps == 1:
                    spread(r,c,x,table)

                if ellaps == x:
                    state = 2
                    ellaps = 0
            #죽음
            else:
                pass

            table[(r,c)] = [state,ellaps,x]


    print("#{} {}".format(test,getRemainArriveCells(table)))

