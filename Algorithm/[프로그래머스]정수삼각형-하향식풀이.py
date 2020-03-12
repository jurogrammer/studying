def Ccl(i, j, memo, triangle):
    if (i, j) in memo:
        return memo[(i, j)]
    else:
        if j == 0:
            memo[(i, j)] = triangle[i][j] + Ccl(i - 1, j, memo, triangle)
        elif i == j:
            memo[(i, j)] = triangle[i][j] + Ccl(i - 1, j - 1, memo, triangle)
        else:
            memo[(i, j)] = triangle[i][j] + max(Ccl(i - 1, j - 1, memo, triangle), Ccl(i - 1, j, memo, triangle))
        return memo[(i,j)]

def solution(triangle):
    memo = {(0, 0): triangle[0][0]}
    i = len(triangle)-1

    maxValue = 0
    for j in range(i):
        Ccl(i, j, memo, triangle)  # i,j 메모 구하셈!
        if maxValue < memo[(i, j)]:
            maxValue = memo[(i, j)]

    answer = maxValue
    return answer
