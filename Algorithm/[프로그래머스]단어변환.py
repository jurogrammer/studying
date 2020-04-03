def FindCsdList(begin,words):
    csdList = []
    n = len(begin)
    for word in words:
        cnt = 0
        for i in range(n):
            if begin[i] != word[i]:
                cnt += 1
        if cnt == 1:
            csdList.append(word)
    return csdList

def solution(begin, target, words):
    if begin == target:
        return 0

    words = set(words)

    repTime = len(words)-1
    flag = False

    csdList = FindCsdList(begin,words)

    curStack = []
    for csdBegin in csdList:
        if csdBegin == target:
            return 1
        curStack.append([csdBegin,words-{csdBegin}])

    for rep in range(repTime):
        nxtStack = []
        while curStack:
            csdBegin,remainWords = curStack.pop()
            csdList = FindCsdList(csdBegin,remainWords)
            for nxtBegin in csdList:
                if nxtBegin == target:
                    return rep+2
                nxtStack.append([nxtBegin,words-{nxtBegin}])
        curStack = nxtStack

    return 0