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
//	for (int i = 0; i < N; ++i) { //��� ���� �湮�� ������ �ݺ�!!
//		/*Si�� ���Ե��ִ� ���±����� �ִܰŸ� �� ���� ª�� ��� ����.*/
//		int minCost = INF, minVertex; // 1~N-1�� �湮�� ���� ��, �˰� �ִ� ���� �ּ��� �� ����.
//		for (int j = 0; j < N; ++j) {
//			if (!visited[j] && Dist[j] < minCost) {
//				minCost = Dist[j];
//				minVertex = j;
//			}
//		}// �湮�� ���� �� �˰��ִ� ��(Dist[j])�� �ּ��� �� ��������. �װ��� minCost = Dist[j], minVertex = j��.
//		/*���� ª�� ��� ��������!*/
//
//		/*���� ª�� ��θ� �����ߴٰ� �ϸ�, ���� �� ª�� ��ο��� �� �� �ִ� ���� ���� �� �� ��.   ������ �ȵǾ� �ִٸ� �������� �̹� ����.*/
//		visited[minVertex] = true; // �� j�� �湮�ߴٰ� �ϰ�,

//		for (int j = 0; j < N; ++j) { //Si-1�ܰ迡�� �ִܰŸ����̶�� �˰� �ִ� Dist[j]��  // minVertex��ġ+minvertex->j �� ���Ͽ� �ִܰŸ���� �ֽ�ȭ.
//			if (Dist[j] > Dist[minVertex] + Graph[minVertex][j])
//				Dist[j] = Dist[minVertex] + Graph[minVertex][j];
//		}
//	}
//
//	
//}