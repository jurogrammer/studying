class oneHeap:
    def __init__(self,n):
        self.n = 0
        self.heap = [0 for _ in range(n+1)]

    def insertNode(self, node):
        self.n += 1
        curIdx = self.n
        parentIdx = curIdx // 2
        item = node

        while self.heap[parentIdx] < item and curIdx != 1:
            self.heap[curIdx] = self.heap[parentIdx]
            curIdx = parentIdx
            parentIdx = curIdx // 2
        self.heap[curIdx] = node

    def pop(self):
        return self.heap[1]


class tupleHeap:
    def __init__(self,n):
        self.n = 0
        self.heap = [(0,0) for _ in range(n+1)]

    def insertNode(self,node):
        self.n += 1
        curIdx = self.n
        parentIdx = curIdx//2
        item = node[0]

        while self.heap[parentIdx][0]<item and curIdx != 1:
            self.heap[curIdx] = self.heap[parentIdx]
            curIdx = parentIdx
            parentIdx = curIdx//2

        self.heap[curIdx] = node

    def returnBuldingNums(self, val):  # heap에서 val 초과인 building 값들을 모두 받기 이는 tuple함수만 이용가능
        buldings = oneHeap(self.n)

        def _recursiveValue(i, target):  # 재귀적으로 탐색하여 val보다 큰 값을 찾아 받음. 초기 루트부터 탐색. node = 1
            nonlocal buldings
            if i > self.n:
                return

            item = self.heap[i][0]
            if item > target:
                buldings.insertNode(self.heap[i][1])  # node[1]은 빌딩번호.
                _recursiveValue(i * 2, target)
                _recursiveValue(i * 2 + 1, target)
            else:
                return

        _recursiveValue(1, val)

        return buldings

n = int(input())
inputBuildings = list(map(int,input().split()))
passBuldings = tupleHeap(n)

for i in range(1,n+1):
    passBuldings.insertNode((inputBuildings[i-1],i))
    print(passBuldings.returnBuldingNums(inputBuildings[i-1]).pop(),end = " ")
