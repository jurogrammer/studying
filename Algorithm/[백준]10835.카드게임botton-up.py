'''
top-down 방식으로 접근.
'''
import sys
sys.setrecursionlimit(1000000)
n = int(input())

leftCards = list(map(int,input().split()))
rightCards = list(map(int,input().split()))

dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

def sol(leftIdx,rightIdx):
    if leftIdx == n or rightIdx == n:
        return 0
    if dp[leftIdx][rightIdx] != -1:
        return dp[leftIdx][rightIdx]
    else:
        dp[leftIdx][rightIdx] = max(sol(leftIdx+1,rightIdx),sol(leftIdx+1,rightIdx+1)) #우선 case1,case2 고려.
        if leftCards[leftIdx] > rightCards[rightIdx]:
            dp[leftIdx][rightIdx] = max(dp[leftIdx][rightIdx],sol(leftIdx,rightIdx+1)+rightCards[rightIdx])

        return dp[leftIdx][rightIdx]

print(sol(0,0))