'''
Nodes = []
distDict : key : (node1,node2) value : 거리
'''
def CclDist(Node1,Node2):
    x1,y1 = Node1
    x2,y2 = Node2
    return abs(x1-x2)+abs(y1-y2)

def FindMinDist(cur,used,N,home,path): #cur : 현재위치 => Nodes[i]값, used : 이동한 곳 비트표현, val : 누적값 N : 노드 수
    if used == (1<<N)-1:
        return CclDist(cur,home)
    else:
        rst = 9999
        for next in range(N):
            if not (used &(1<<next)) :
                temp = CclDist(cur,Nodes[next]) + FindMinDist(Nodes[next],used|(1<<next),N,home,path+str(next))
                print(path , ":",temp,"mext",next)
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

    rst = 9887

    for sNode in range(N):
        temp = CclDist(company,Nodes[sNode])+ FindMinDist(Nodes[sNode],1<<sNode,N,home,'')
        if rst>temp:
            rst = temp

    print(rst)


# total = CclDist(company,Nodes[1])
# x = [1,3,4,0,5,6,2]
# for i in range(len(x)):
#     if i == 6:
#         break
#     print(total)
#     total += CclDist(Nodes[x[i]],Nodes[x[i+1]])
# print(total)
#
# total += CclDist(Nodes[6],home)
# Nodes