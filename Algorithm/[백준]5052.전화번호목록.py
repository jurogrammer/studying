import sys

input = sys.stdin.readline


class NODE:
    def __init__(self):
        self.value = False  # true면 값이 존재
        self.childs = [False for _ in range(10)]


class TRI:
    def __init__(self):
        self.root = NODE()

    '''
    가독성은 떨어지나... 넣다가 중도에 value가 True값 만나면 그대로 종료.
    따라서 return 값은 True or False
    이떄 조건은 정렬되어 있어야 한다. 안그러면 1111,11 이 케이스에서 True나옴.

    for문에서 true나 false받은거 처리하기
    '''

    # root는 childs만 가진다.
    def insertValue(self, bookNumber):
        curNode = self.root

        # curNode를 탐색할건데 값이 없으면 생성.
        for number in bookNumber:
            number = int(number)
            if not curNode.childs[number]:
                curNode.childs[number] = NODE()

            curNode = curNode.childs[number]
            if curNode.value is True:
                return False

        # for문을 빠져나왔다는 건 중복값이 없었고 마지막 문자 노드에 왔단 의미.
        curNode.value = True
        return True


testCase = int(input().rstrip())

for t in range(testCase):
    n = int(input().rstrip())
    bookNumList = [input().rstrip() for _ in range(n)]
    bookNumList.sort()
    tri = TRI()

    for bookNum in bookNumList:
        isOK = tri.insertValue(bookNum)
        if not isOK:
            break

    if isOK:
        print("YES")
    else:
        print("NO")