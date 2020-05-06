from queue import PriorityQueue
from collections import deque

class MaxPQ:
    def __init__(self):
        self.pq = PriorityQueue()

    def put(self,num):
        self.pq.put(-num)

    def get(self):
        return -self.pq.get()

    def isEmpty(self):
        return self.pq.empty()

def solution(priorities, location):
    #1. priorities 우선순위 큐에 담기
    pq = MaxPQ()
    for p in priorities:
        pq.put(p)

    #2. priorities를 index과 결부
    n = len(priorities)
    waitingDocs = deque(zip(priorities,range(n))) #우선순위, index

    #3. priorities의 앞 값이 우선순위 큐의 값과 동일하다면 pop
    turn = 0
    while True:
        #일단 해당 경우 빼봐
        priority, index = waitingDocs.popleft()
        curMaxPriority = pq.get()

        #뺏을 때 우선순위가 가장 높지 않으면 다시 집어넣어
        if priority != curMaxPriority:
            waitingDocs.append((priority,index))
            pq.put(curMaxPriority)

        #그게 아니면 그대로 빼.
        else:
            turn += 1
            #그런데 찾으려는 인덱스도 동일해? 그럼 굳.
            if index == location:
                break

    answer = turn
    return answer

priorities = [1,2,3,4]
location = 2
