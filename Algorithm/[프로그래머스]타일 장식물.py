memo = {0:0,1:1,2:1}

def pibo(N):
    if N not in memo :
        memo[N] = pibo(N-1) + pibo(N-2)
    return
    
def solution(N):
    if N == 1:
        return 4
    pibo(N)
    
    answer = memo[N]*4+memo[N-1]*2
    
    return answer
