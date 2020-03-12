//#include <stdio.h>
//#define MAX_N 10
//#define INF 1000000
//int N, Graph[MAX_N][MAX_N], Dist[MAX_N];
//void dijkstra(int start) {
//	bool visited[MAX_N] = { false };
//	for (int i = 0; i < N; ++i)
//		Dist[i] = INF;
//	Dist[start] = 0;
//
//	for (int i = 0; i < N; ++i) { //모든 정점 방문할 때까지 반복!!
//		/*Si에 포함되있는 여태까지의 최단거리 중 가장 짧은 경로 선택.*/
//		int minCost = INF, minVertex; // 1~N-1의 방문한 정점 중, 알고 있는 값이 최소인 점 선택.
//		for (int j = 0; j < N; ++j) {
//			if (!visited[j] && Dist[j] < minCost) {
//				minCost = Dist[j];
//				minVertex = j;
//			}
//		}// 방문한 정점 중 알고있는 값(Dist[j])이 최소인 것 선택했음. 그것의 minCost = Dist[j], minVertex = j임.
//		/*가장 짧은 경로 선택했음!*/
//
//		/*가장 짧은 경로를 선택했다고 하면, 이제 그 짧은 경로에서 갈 수 있는 곳과 기존 값 값 비교.   연결이 안되어 있다면 무한으로 이미 설정.*/
//		visited[minVertex] = true; // 그 j를 방문했다고 하고,

//		for (int j = 0; j < N; ++j) { //Si-1단계에서 최단거리값이라고 알고 있는 Dist[j]와  // minVertex위치+minvertex->j 와 비교하여 최단거리라면 최신화.
//			if (Dist[j] > Dist[minVertex] + Graph[minVertex][j])
//				Dist[j] = Dist[minVertex] + Graph[minVertex][j];
//		}
//	}
//
//	
//}