def GetMultipleSet(string):
    n = len(string)
    multipleSet = {}
    string = string.lower()
    for i in range(1, n):
        if string[i].isalpha() and string[i - 1].isalpha():
            element = string[i] + string[i - 1]
            if element in multipleSet:
                multipleSet[element] += 1
            else:
                multipleSet[element] = 1
    return multipleSet


def GetIntersectionNum(multiSet1, multiSet2):
    total = 0

    for m1 in multiSet1:
        if m1 in multiSet2:
            total += min(multiSet1[m1], multiSet2[m1])

    return total


def GetUnionNum(multiSet1, multiSet2):
    total = 0
    visited = set()
    for m1 in multiSet1:
        if m1 in multiSet2:
            total += max(multiSet1[m1], multiSet2[m1])
            visited.add(m1)
        else:
            total += multiSet1[m1]

    for m2 in multiSet2:
        if m2 in visited:
            continue
        total += multiSet2[m2]

    return total


def solution(str1, str2):
    multiSet1 = GetMultipleSet(str1)
    multiSet2 = GetMultipleSet(str2)
    intersectionNum = GetIntersectionNum(multiSet1, multiSet2)
    unionNum = GetUnionNum(multiSet1, multiSet2)
    jarcard = 0

    if not multiSet1 and not multiSet2:
        jarcard = 1
    else:
        jarcard = intersectionNum/unionNum

    answer = int(jarcard*65536)
    return answer