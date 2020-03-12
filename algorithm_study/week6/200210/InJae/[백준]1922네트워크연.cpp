//#include <stdio.h>
//#include <stdlib.h>
//#define INF 10001 //����� �ִ밪�� 10,000�̹Ƿ� ���� ���� ���� 10001�� ǥ���Ѵ�.
//
//int prim(int** graph, int N) //graph�� adjency matrix, N�� node��+1
//{	
//	/*int weight[N] = { 0, };
//	int parents[N] = { 0, }; */
//
//	int* weight = (int*)malloc(sizeof(int) * N);
//	int* parents = (int*)malloc(sizeof(int) * N);
//
//	
//	for (int i = 0; i < N; i++) //��� ���õ��� �ʾҴٰ� ����. ����ġ -1�� �ʱ�ȭ.   **0�� �ε����� ������� �ʴ� vertex�̹Ƿ� ���߿� �ʱ�ȭ. �� 0���� �α⿣ �ʱ� vertex���ý� 0���� �ؾ���.
//		weight[i] = -1;
//	weight[1] = 0;
//	for (int rep = 1; rep < N-1; rep++)
//	{
//		int minVertex;
//		int minParent;
//		int minWeight = INF;
//		for (int i = 1; i < N; i++) //V(MST_r) ����.
//		{
//			if (weight[i] < 0) continue;
//			for (int j = 1; j < N; j++) // ~V(MST_r)����.
//			{
//				if (weight[j] >= 0) continue;
//				if (graph[i][j] < minWeight) {
//					minWeight = graph[i][j]; minParent = i; minVertex = j;
//				}
//
//			}
//			
//		}
//
//
//		parents[minVertex] = minParent;
//		weight[minVertex] = minWeight;
//	}
//
//	int total = 0;
//	for (int i = 1; i < N; i++)
//	{
//		total += weight[i];
//	}
//		
//	free(weight);
//	free(parents);
//	return total;
//		
//}	
//
//
//int main(void)
//{
//	int N;
//	scanf("%d", &N);
//	N++; //arr[i][j]�� i��° 
//	int** graph = (int**)malloc(sizeof(int*) * N);
//	for (int i = 0; i < N; i++)
//		graph[i] = (int*)malloc(sizeof(int) * N);
//
//	for (int i = 0; i < N; i++)
//		for (int j = 0; j < N; j++)
//			graph[i][j] = INF;
//
//	int M;
//	scanf("%d", &M);
//	for (int i = 0; i < M; i++)
//	{
//		int a, b, c;
//		scanf("%d %d %d", &a, &b, &c);
//		graph[a][b] = c;
//		graph[b][a] = c;
//	}
//
//	/*for (int i = 0; i < N; i++)
//		for (int j = 0; j < N; j++)
//			printf("graph[%d][%d] = %d\n", i, j, graph[i][j]);*/
//	
//	printf("%d\n", prim(graph, N));
//	free(graph);
//	return 0;
//}		