'''
STEP1. 그래프 받기
STEP2. 다익스트라로 최단경로 찾기
STEP3. 최단 경로의 값 알기
STEP4. 지나온 최단경로를 GRAPH에서 INF값으로 바꿔주기
STEP5. 다익스트라 재적용 -> 만약 최단경로 값과 일치한다면 STEP2,4반복
                         -> 일치하지 않는다면 해당 값 출력.
'''
INF = 987654321
N,M = map(int,input().split()) #N : 노드 수 (장소의 수) M : 도로의 수
S,D = map(int,input().split()) #S : 출발 노드 D : 도착노드

graph = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    u,v,p = map(int,input().split())
    graph[u][v] = p


for _ in range(n):
    
