def parsing(s): #return은 정렬된 값
    # parsing작업
    s = s[2:-2]
    s = s.split("},{")
    parsingList = list(s)  # return 형태  ['2,1,3,4', '2', '2,1', '2,1,3']
    n = len(parsingList)
    sortedSets = []
    for i in range(n):
        sortedSets.append(set(parsingList[i].split(',')))

    return sorted(sortedSets)



def solution(s):
    answer = []

    sortedSets = parsing(s)
    n = len(sortedSets)
    item = sortedSets[0].copy()
    answer.append(int(item.pop()))
    for i in range(1,n):
        item = sortedSets[i]-sortedSets[i-1]
        answer.append(int(item.pop()))

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))