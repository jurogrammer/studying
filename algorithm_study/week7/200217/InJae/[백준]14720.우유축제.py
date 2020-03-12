def sol(n,stores):
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    stores = [0] + stores
    for i in range(1,n+1):
        if  stores[i] == 0:
            dp[i][0] = max(dp[i-1][0],dp[i-1][2]+1)
        else:
            dp[i][0] = dp[i-1][0]

        if  stores[i] == 1:
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+1)
        else:
            dp[i][1] = dp[i-1][1]
        if dp[i][1] == 1:
            dp[i][1] = 0

        if  stores[i] == 2:
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+1)
        else:
            dp[i][2] = dp[i-1][2]
        if dp[i][2] == 1:
            dp[i][2] = 0
    ans = 0
    for i in range(3):
        ans = max(ans,dp[n][i])
    return ans

n = int(input())
stores = list(map(int,input().split()))
print(sol(n,stores))