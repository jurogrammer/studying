def solution(triangle):
    answer = 0
    h = len(triangle)
    for i in range(1,h):
        for j in range(i+1):
            if j == 0 :
                triangle[i][j] = triangle[i-1][j]+triangle[i][j]
            elif j == i :
                triangle[i][j] = triangle[i-1][j-1]+triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1],triangle[i-1][j])+triangle[i][j]

    answer = max(triangle[-1])
    return answer

