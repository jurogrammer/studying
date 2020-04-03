class PQ:
    def __init__(self):
        self.pq = [[-1,-1] for _ in range(501)]
        self.n = 0

    def push(self, item):
        self.n += 1
        i = self.n
        while i != 1 and item[1] < self.pq[i // 2][1]:
            self.pq[i] = self.pq[i // 2]
            i = i // 2
        self.pq[i] = item

    def pop(self):
        val = self.pq[1]
        item = self.pq[self.n]
        self.n -= 1
        p = 1
        c = 2
        while c <= self.n:
            if self.pq[c][1] > self.pq[c + 1][1]:
                c = c + 1
            if item[1] <= self.pq[c][1]:
                break
            self.pq[p] = self.pq[c]
            p = c
            c = p * 2
        self.pq[p] = item
        return val

    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False


def solution(jobs):
    jobs.sort()
    jobLength = len(jobs)
    pq = PQ()

    accTime = 0
    waitingTime = 0
    i = 0
    while i < jobLength:
        if jobs[i][0] <= accTime:
            pq.push(jobs[i])
            i += 1
        else:
            break

    while i < jobLength:

        #1.꺼내서 처리하기. 시간이 흐른다.
            #1-1. 큐가 비어있는 경우,
        if pq.isEmpty():
            accTime = jobs[i][0] + jobs[i][1]
            waitingTime = waitingTime + jobs[i][1]
            i += 1
            #1-2. 큐에 값이 있는 경우.
        else:
            requestTime,processingTime = pq.pop()
            accTime = accTime + processingTime
            waitingTime = waitingTime + (accTime - requestTime)


        while i < jobLength :
            if jobs[i][0] <= accTime :
                pq.push(jobs[i])
                i += 1
            else:
                break

    while not pq.isEmpty():
        requestTime,processingTime = pq.pop()
        accTime = accTime + processingTime
        waitingTime = waitingTime + (accTime - requestTime)

    answer = waitingTime//jobLength
    return answer

jobs = [[1,1],[1,2]]

print(solution(jobs))