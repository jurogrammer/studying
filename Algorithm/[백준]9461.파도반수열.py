'''
https://jurogrammer.tistory.com/6
'''


memo = {1:1,2:1,3:1}

def Wave(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = Wave(n-2)+Wave(n-3)
        return memo[n]

n = int(input())
for _ in range(n):
    req = int(input())
    print(Wave(req))