'''
Nodes = []
distDict : key : (node1,node2) value : 거리
'''
def CclDist(Node1,Node2):
    x1,y1 = Node1
    x2,y2 = Node2
    return abs(x1-x2)+abs(y1-y2)


def FindMinDist(cur,used,val,N,home): #cur : 현재위치 => Nodes[i]값, used : 이동한 곳 비트표현, val : 누적값 N : 노드 수
    if used == ((1<<N)-1):
        return val + CclDist(cur,home)
    else:
        rst = 9999999

        for i in range(N):
            if (used &(1<<i)): continue
            else:
                temp = FindMinDist(Nodes[i],used|(1<<i),val + CclDist(cur,Nodes[i]),N,home)
                if rst>temp:
                    rst = temp
    return rst

test = int(input())
for _ in range(test):
    N = int(input())
    inputList = list(map(int,input().split()))
    Nodes = [[0,0] for _ in range(N)]

    company = (inputList[0],inputList[1])
    home = (inputList[2],inputList[3])

    xIdx = 4
    yIdx = 5
    for i in range(N):
        Nodes[i][0] = inputList[xIdx]
        Nodes[i][1] = inputList[yIdx]
        xIdx += 2
        yIdx += 2

    print(FindMinDist(company,0,0,N,home))



