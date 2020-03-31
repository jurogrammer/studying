def rotate(circle,k,d,m):
    if d == 0:
        return circle[m-k:]+circle[:m-k]

    else:
        return circle[k:]+circle[:k]

N,M,T = map(int,input().split())
circles = [[0]*M]
totalNumbers = N*M
direction = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(N):
    circles.append(list(map(int,input().split())))

for z in range(T):
    x,d,k = map(int,input().split())

    for i in range(1,N+1): #회전
        if i%x == 0 :
            circles[i] = rotate(circles[i],k,d,M)
    #인접탐색
    sumNumbers = 0
    ajflag = False

    delList = set()
    for i in range(1,N+1):
        for j in range(M):
            number = circles[i][j]
            flag = False
            if number == 0:
                continue

            #해당 i,j에 대해 인접 탐색
            for di,dj in direction:
                ni = i+di
                nj = j+dj
                if nj == -1 :
                    nj = M-1
                elif nj == M:
                    nj = 0

                if ni<=0 or ni>N : #i의 0은 수채우기용, N번째까지 존재, j는 0번에서 M-1까지 존재.
                    continue

                ajNumber = circles[ni][nj] #인접 수
                if ajNumber == 0 :
                    continue
                if ajNumber == number: #인접 수가 같다면 삭제해줘야 함. 삭제한다는 것은 0을 의미한다.
                    flag = True
                    delList.add((ni,nj))

            if flag: #삭제가 발생했다면 i,j 위치 삭제해주고 전체 수 삭제
                delList.add((i,j))
                ajflag = True

    if delList:
        for delI,delJ in delList:
            circles[delI][delJ] = 0



    totalNumbers = totalNumbers - len(delList)
    if totalNumbers == 0 :
        break

    sumNumbers = 0
    for i in range(1,N+1):
        sumNumbers+=sum(circles[i])

    avg = sumNumbers/totalNumbers
    if ajflag is False: #삭제가 발생하지 않았다면 평균구해서 가산연산 해줘야 함.
        for i in range(1,N+1):
            for j in range(M):
                if circles[i][j] == 0 :
                    continue
                elif avg>circles[i][j]:
                    circles[i][j] += 1
                elif avg<circles[i][j]:
                    circles[i][j] -= 1
    # 인접탐색
rst = 0
for i in range(1,N+1):
    rst += sum(circles[i])
print(rst)





