def GetBoundary(area,x,y,d1,d2,N,visited):
    try :
        for i in range(d1+1):
            visited[x+i][y-i] = 5
            visited[x+d2+i][y+d2-i] = 5

        for i in range(d2+1):
            visited[x+i][y+i] = 5
            visited[x+d1+i][y-d1+i] = 5

        for i in range(N+2):
            if visited[i][0] != -1 or visited[i][N+1] != -1 or visited[0][i] != -1 or visited[N+1][i] != -1:
                return  False

        return True
    except:
        return False

def GetArea1Population(area,x,y,d1,d2,N,visited):
    total = 0
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if r<=0 or c<=0 or r>N or c>N:
                return 0
            if visited[r][c] == 5:
                break
            total += area[r][c]
            visited[r][c] = 1

    return total

def GetArea2Population(area,x,y,d1,d2,N,visited):
    total = 0
    for r in range(1,x+d2+1):
        for c in range(N,y,-1):
            if r<=0 or c<=0 or r>N or c>N:
                return 0
            if visited[r][c] == 5:
                break
            total += area[r][c]
            visited[r][c] = 2
    return total

def GetArea3Population(area,x,y,d1,d2,N,visited):
    total = 0
    for r in range(x+d1,N+1):
        for c in range(1,y-d1+d2):
            if r<=0 or c<=0 or r>N or c>N:
                return 0
            if visited[r][c] == 5:
                break
            total += area[r][c]
            visited[r][c] = 3

    return total

def GetArea4Population(area,x,y,d1,d2,N,visited):
    total = 0
    for r in range(x+d2+1,N+1):
        for c in range(N,y-d1+d2-1,-1):
            if r<=0 or c<=0 or r>N or c>N:
                return 0
            if visited[r][c] == 5:
                break
            total += area[r][c]
            visited[r][c] = 4
    return total

def GetArea5Population(area,x,y,d1,d2,N,visited):
    total = 0
    for r in range(1,N+1):
        for c in range(1,N+1):
            if visited[r][c] == -1 or visited[r][c] == 5:
                total += area[r][c]

    return total


N = int(input())

area = [[-9999]*(N+2)]+ [[-9999]+list(map(int,input().split()))+[-9999] for _ in range(N)]+[[-9999]*(N+2)]
minVal = 40001

for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1-x):
            for d2 in range(1,N+1-x-d1):
                visited = [[-1 for _ in range(N+2)] for _ in range(N+2)]
                if not GetBoundary(area,x,y,d1,d2,N,visited):
                    continue
                a1 = GetArea1Population(area,x,y,d1,d2,N,visited)
                a2 = GetArea2Population(area, x, y, d1, d2, N, visited)
                a3 = GetArea3Population(area, x, y, d1, d2, N, visited)
                a4 = GetArea4Population(area, x, y, d1, d2, N, visited)
                a5 = GetArea5Population(area, x, y, d1, d2, N, visited)


                values = [a1,a2,a3,a4,a5]
                csdVal = max(values)-min(values)
                if csdVal<minVal:
                    minVal = csdVal

print(minVal)