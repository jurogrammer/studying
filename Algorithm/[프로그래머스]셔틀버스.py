from queue import Queue

def ConvertTimeIntToString(h,m):
    #시
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
    # 분
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    return h + ':' + m

def passTime(curTime,t):
    h = int(curTime[:2])
    m = int(curTime[3:])
    #시간더하기
    if m+t >= 60:
        m = (m+t)-60
        h += 1
    else:
        m += t
    return ConvertTimeIntToString(h,m)

def GetPreTime(time):
    h = int(time[:2])
    m = int(time[3:])

    #숫자로 바꾸기
    if m == 0:
        h -= 1
        m = 59
    else:
        m -= 1
    return ConvertTimeIntToString(h,m)

def solution(n, t, m, timetable):
    answer = ''
    preN = n-1
    timetable.sort()
    tableLen = len(timetable)
    i = 0

    startTime = "09:00"
    que = Queue()
    #막차전까지 모두 태우기
    for _ in range(preN):
        #출발시간 전까지 타임테이블에 있는 사람 세우기
        while i<tableLen and timetable[i]<=startTime:
            que.put(timetable[i])
            i += 1

        #정원수 만큼 대기자 pop!
        tempM = m
        while not que.empty() and tempM != 0:
            que.get()
            tempM -= 1

        startTime = passTime(startTime,t)

    #막차 사람 태우기
    while i<tableLen and timetable[i]<=startTime:
        que.put(timetable[i])
        i += 1

    #정원이 남아있다면 출발때 타기
    if que.qsize()<m:
        answer = startTime
    #정원 초과라면 마지막 대기자 사람보다 1분빨리 오기
    else:
        #마지막 정원자전까지 pop
        tempM = m-1
        while tempM != 0:
            que.get()
            tempM -= 1

        lastPersonTime = que.get()
        answer = GetPreTime(lastPersonTime)

    return answer

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]


print(solution(n,t,m,timetable))