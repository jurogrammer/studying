from queue import Queue

#인접행렬로 만들기엔 2만이므로 공간복잡도가 매우 큼. 2만x2만 -> 4백만.
def ConvertEdgeToGraph(edge):
    #1번 노드부터 시작, 최대 2만개. 그래프는 인덱스가 u,value가 v
    graph = [[] for _ in range(20001)]
    #양방향 그래프
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def solution(n, edge):

# BFS로 탐색하나, 최종 size 기록. 매 size만큼 pop해주는 과정 거치기.
    #초기화
    que = Queue()
    graph = ConvertEdgeToGraph(edge)
    visited = 1<<1
    que.put(1)

    #큐가 빌때까지 반복(마지막까지)
    while not que.empty():
        #사이즈 얻기
        size = que.qsize()
        #사이즈 만큼 pop하고 pop한 vertex에서 다음으로 이동한 것 que에 삽입
        for _ in range(size):
            u = que.get()
            for v in graph[u]:
                if not visited&(1<<v):
                    que.put(v)
                    visited = visited|(1<<v)

    answer = size
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,edge))