from collections import deque

def passDay(progresses,speeds):
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

def getDeployNum(progresses,speeds):
    count = 0
    while progresses and progresses[0] >= 100:
        count += 1
        progresses.popleft()
        speeds.popleft()
    return count


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        passDay(progresses,speeds)
        count = getDeployNum(progresses,speeds)
        if count :
            answer.append(count)

    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses,speeds))