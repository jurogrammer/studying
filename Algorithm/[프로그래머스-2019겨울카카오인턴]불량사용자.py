class NODE:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

def inserValue(root,id):
    curNode = root
    for char in id:
        if char not in curNode.children:
            curNode.children[char] = NODE()
        curNode = curNode.children[char]
    curNode.endOfWord = True

def FindPossibleValues(bId, rootNode):
    initChar = bId[0]
    curStack = []  # 원소 노드,여태까지 문자
    if initChar == "*":
        for key in rootNode.children:
            curStack.append((key, rootNode.children[key]))
    else:
        curStack.append((initChar, rootNode.children[initChar]))

    for char in bId[1:]:
        nxtStack = []
        if char == '*':
            while curStack:
                subString, curNode = curStack.pop()
                for key in curNode.children:
                    nxtStack.append((subString + key, curNode.children[key]))
        else:
            while curStack:
                subString, curNode = curStack.pop()
                if char not in curNode.children:
                    continue
                nxtStack.append((subString + char, curNode.children[char]))

        curStack = nxtStack

    possibleValues = []
    for uid,node in curStack:
        possibleValues.append(uid)
    return possibleValues

def solution(user_id, banned_id):
    answer = 0
    rootNode = NODE()

    for uId in user_id:
        inserValue(rootNode,uId)

    banned_id = banned_id
    user_id = set(user_id)

    rst = set()
    def CountAnswer(user_id,banned_id,rootNode):
        nonlocal answer
        if not banned_id:
            user_id = list(user_id)
            user_id.sort()
            rst.add(tuple(user_id))
            return

        bId = banned_id.pop()
        possibleValues = FindPossibleValues(bId,rootNode)

        for possibleUId in possibleValues:
            if possibleUId not in user_id:
                continue
            CountAnswer(user_id-{possibleUId},banned_id.copy(),rootNode)

    CountAnswer(user_id,banned_id,rootNode)

    answer = len(rst)
    return answer