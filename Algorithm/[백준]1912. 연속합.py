'''
jurogrammer.tistory.com/3
'''
n = int(input())
nums = list(map(int,input().split()))
dp = [0 for _ in range(n)]

rst = nums[0] #초기 최대 값 설정
dp[0] = nums[0] #0번째 초기화. i-1번째를 볼 것이므로 0번째 초기화 후 1번째부터 풀이

for i in range(1,n):
    dp[i] = max(nums[i],nums[i]+dp[i-1])
    if dp[i]>rst:
        rst = dp[i]

print(rst)