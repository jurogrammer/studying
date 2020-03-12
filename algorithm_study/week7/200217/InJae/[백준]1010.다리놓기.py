import sys
memo  = {(0,0):1,(1,0):1,(1,1):1}
input = sys.stdin.readline
def func(m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    if m < 0 or n < 0:
        return 0

    else:
        memo[(m, n)] = func(m - 1, n) + func(m - 1, n - 1)
    return memo[(m, n)]

t = int(input())
for i in range(30):
    func(30, i)


for _ in range(t):
    N,M = map(int,input().split())
    print(func(M,N))