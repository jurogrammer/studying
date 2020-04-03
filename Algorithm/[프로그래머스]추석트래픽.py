def ConvertlogToSPTime(log):
    day, rspTime, prcTime = log.split(" ")
    #종료시간
    endTime = rspTime
    h,m,s = rspTime.split(":")

    #시작시간
        #수로 만들어주기
    h,m,s = int(h),int(m),float(s)
    prcTime = float(prcTime.rstrip("s"))
        #값 차이 구하기

    if (s - prcTime + 0.001) < 0:
        m -= 1
        s = 60 + (s - prcTime + 0.001)
        if m < 0 :
            if h == 0:
                return "00:00:00.000",endTime
            else:
                h -= 1
                m = 59
    else:
        s = s-prcTime+0.001

    s = round(s,3)

    #문자로 만들어주기
    if h < 10:
        h = '0'+str(h)
    else:
        h = str(h)
    if m < 10:
        m = '0'+str(m)
    else:
        m = str(m)
    if s < 10:
        s = '0'+str(s)
    else:
        s = str(s)

    startTme = ":".join((h,m,s))

    return startTme,endTime

def PassOneSecond(time):
    h,m,s = time.split(":")
    h = int(h)
    m = int(m)
    s = float(s)
    s = s + 0.999
    if s>=60:
        m += 1
        s = s-60

        if m>=60:
            h += 1
            m = 0

    s = round(s, 3)

    #문자로 만들어주기
    if h < 10:
        h = '0'+str(h)
    else:
        h = str(h)
    if m < 10:
        m = '0'+str(m)
    else:
        m = str(m)
    if s < 10:
        s = '0'+str(s)
    else:
        s = str(s)

    passedTime = ":".join((h,m,s))
    return passedTime

def solution(lines):
    answer = 0
    spTimes = [ConvertlogToSPTime(log) for log in lines]
    spTimes.sort(key = lambda a : (a[1],a[0]))

    for csdStart,csdEnd in spTimes:
        cnt = 0
        #csdStart
        start = csdStart
        end = PassOneSecond(csdStart)
        for objStart, objEnd in spTimes:
            if start <= objStart <= end or start <= objEnd <= end or (objStart <= start and end<=objEnd):
                cnt += 1
        if answer < cnt:
            answer = cnt

        cnt = 0
        #csdEnd
        start = csdEnd
        end = PassOneSecond(csdEnd)
        for objStart, objEnd in spTimes:
            if start <= objStart <= end or start <= objEnd <= end or (objStart <= start and end<=objEnd):
                cnt += 1
        if answer < cnt:
            answer = cnt

    return answer

lines = ['2016-09-15 23:59:59.599 1s','2016-09-15 23:59:59.010 0.5s','2016-09-15 23:59:58.111 0.001s']

print(solution(lines))