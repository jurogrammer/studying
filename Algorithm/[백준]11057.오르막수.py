'''
https://jurogrammer.tistory.com/8
'''
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)] # 편의를 위해 1번째 인덱스부터 고려하기.

for i in range(10): #초기 값 설정
    dp[1][i] = 1

for step in range(1,n+1):
    dp[step][0] = 1
    for k in range(1,10):
        dp[step][k] = (dp[step][k-1]%10007 + dp[step-1][k]%10007)%10007

print(sum(dp[n])%10007)