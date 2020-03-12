lost = [3]
reserve = [1]

def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    while lost and reserve:
        giver = reserve.pop()
        if giver in lost:
            lost.remove(giver)
            continue

        else:
            rcv1 = giver-1
            rcv2 = giver+1
            if rcv1 in lost and rcv1 not in reserve:
                lost.remove(rcv1)
            elif rcv2 in lost and rcv2 not in reserve:
                lost.remove(rcv2)

    answer = n - len(lost)
    return answer

print(solution(n,lost,reserve))
