def FindSet(node,parents):
    if node not in parents:
         return -1

    curNode = node
    childList = []
    while parents[curNode] != curNode:
        childList.append(curNode)
        curNode = parents[curNode]

    for child in childList:
        parents[child] = curNode

    return curNode

def UnionSet(root1,root2,parents): #root값이 -1이면 존재하지 않는 값.
    if root1 == -1 or root2 == -1 :
        return -1

    parents[root1] = root2
    return

def solution(k, room_number):
    answer = []
    parents = {}
    for room in room_number:
        leftRoot = -1
        #1.room이 들어갈 자리 찾기
        if room not in parents:
            insertedRoot = room
        else:
            leftRoot = FindSet(room,parents)
            insertedRoot = leftRoot + 1

        #2.루트노드는 자기 자신이 담겨야 함.
        parents[insertedRoot] = insertedRoot
        #3.answer에 값담기
        answer.append(insertedRoot)

        #4.찾은 자리 기준 unionFind 실시
            #4-1. 왼쪽노드찾기.   000x 0이 값이 존재한 곳이라면 왼쪽으로부터 3번째 0위치가 값넣는 x기준 왼쪽.
        if leftRoot == -1:
            leftRoot = FindSet(insertedRoot-1, parents)
        rightRoot = FindSet(insertedRoot + 1, parents)

        UnionSet(leftRoot,insertedRoot,parents)
        UnionSet(insertedRoot,rightRoot,parents)

    return answer