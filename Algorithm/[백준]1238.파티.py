def FindAllCost(cost, n): # cost : graph, n : vertex 수
    distance = [cost[i][:] for i in range(n) ]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

INF = 987654321

n,m,x = map(int,input().split())
cost = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u,v,t = map(int,input().split())
    cost[u-1][v-1] = t

for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = 0

shotDistnce = FindAllCost(cost,n)

for i in range(n):
    print(shotDistnce[i])

print("==")

def dijkstra(cost,n):
    dist = [INF for _ in range(n)]
    dist[0] = 0
    visited = [False for _ in range(n)]

    for _ in range(n):

        minCost = 9877
        minVertex = -1
        for i in range(n):
            if not visited[i] and dist[i]<minCost:
                minCost = dist[i]
                minVertex = i

        visited[minVertex] = True
        for v in range(n):
            if dist[minVertex] + cost[minVertex][v] < dist[v]:
                dist[v] = dist[minVertex] + cost[minVertex][v]

    return dist

print(dijkstra(cost,n))