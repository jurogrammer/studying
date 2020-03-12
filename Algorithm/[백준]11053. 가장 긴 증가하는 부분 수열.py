'''
https://jurogrammer.tistory.com/4
'''
n = int(input())
nums = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

rst = 1
for i in range(1,n):
    maxVal = 0
    for j in range(i):
        if nums[i]>nums[j] and maxVal < dp[j]:
            maxVal = dp[j]
    dp[i] = maxVal + 1
    if rst<dp[i]:
        rst = dp[i]

print(rst)
