N,M = map(int,input().split())
workDay = set(map(int,input().split()))
INF = 98798765
oneDayFee = 10000
threeDayFee = 25000
fiveDayFee = 37000
notVisited = 99999999
cNum = int((N/5)*2+5)
dp = [[notVisited for _ in range(cNum+1)] for _ in range(N+1)]

#존재할 수 없는 값 처리.
'''
쿠폰의 수는... 5일째 -> 2개 3일째 -> 1개 그 이상은 불가.
6일째 -> 2개 가능
7일째 -> 2개 가능
9일째 -> 3개 가능.
10일째 -> 4개 가능

if c>min(d//3*2,d//5*2):
'''
for c in range(cNum+1):
    for d in range(N+1):
        if c > min(d // 3 * 2, d // 5 * 2):
            dp[d][c] = INF

dp[0][0] = 0
def func(d,c):
    if d<0 or c<0 or c>cNum:
        return INF

    if d in workDay:
        return func(d-1,c)

    if dp[d][c] != notVisited:
        return dp[d][c]


    ans1 = min(func(d-1,c+3),func(d-1,c)+oneDayFee)
    ans2 = func(d-3,c-1)+threeDayFee
    ans3 = func(d-5,c-2)+fiveDayFee

    dp[d][c] = min(ans1,ans2,ans3)
    return dp[d][c]

ans = []
for i in range(cNum+1):
    ans.append(func(N,i))
print(min(ans))