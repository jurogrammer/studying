def solution(m, n, puddles):
    puddleCheck = [[0]*(m+1) for _ in range(n+1)]
    table = [[0]*(m+1) for _ in range(n+1)]
    table[1][1] = 1

    for c,r in puddles: #puddle 표시
        puddleCheck[r][c] = 1 #

    for r in range(1,n+1):
        for c in range(1,m+1):
            if r==1 and c == 1:
                continue
                
            if puddleCheck[r][c] == 1 :
                continue

            else :
                table[r][c] = (table[r-1][c] + table[r][c-1])%1000000007


    return table[-1][-1]
