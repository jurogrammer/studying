import sys
input = sys.stdin.readline
N,T = map(int,input().split())
times = [0]
scores = [0]
for _ in range(N):
    t,s = map(int,input().split())
    times.append(t)
    scores.append(s)

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(N+1): #i번째,
    for t in range(T+1): #전체 배낭무게가 t일 때!
        if i<0 or t<0:
            continue
        if times[i-1] <= t:
            dp[i][t] = max(dp[i-1][t-times[i-1]]+scores[i-1],dp[i-1][t])
        else:
            dp[i][t] = dp[i-1][t]

print(max(dp[N]))