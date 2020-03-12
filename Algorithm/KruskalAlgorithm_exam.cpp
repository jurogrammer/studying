///*
//Kruskal Algorithm!
//
//Edge�� �������� ����
//edge�� ���� ���� ������ �����ؼ� MST ����. -> n-1�ݺ��Ͽ� edge���� �ؾ���.
//
//edge�� struct�� ǥ��. u,v,weight
//
//parents ������ ���� ����Ŭ���� �Ǵ�
//
//����Ŭ �Ǵܹ�
//u�� v�� ���� ����̸� ����.
//
//*/
//#include <stdio.h>
//#include <stdlib.h>
//
//
//#define MAX_Edge 100001
//#define MAX_Vertex 1001
//struct Edge_type {
//	int u;
//	int v;
//	int cost;
//};
//
//void swap(struct Edge_type* edge1, struct Edge_type* edge2) {
//	struct Edge_type temp;
//	temp = *edge1;
//	*edge1 = *edge2;
//	*edge2 = temp;
//}
//
//int GetPivot(struct Edge_type arr[], int l, int r) {
//	int p = arr[r].cost;
//	int i = l - 1; //idx of smaller than pivot  inition Value is left - 1 beacause of empty
//
//	for (int j = l; j < r; j++) {
//		if (arr[j].cost < p)
//			swap(&arr[++i], &arr[j]);
//	}
//	/* �� ����ص� i�� ���� ���� ���� ��ġ�� ��Ÿ��. �׷��� 1���� ��Ų ���� pivot�� ��ȯ�Ͽ� pivot�� �� �������� �������. */
//	swap(&arr[++i], &arr[r]);
//	return i;
//}
//
//void QuickSort(struct Edge_type arr[], int l, int r) {
//	if (l < r) {
//		int pi = GetPivot(arr, l, r);
//
//		QuickSort(arr, l, pi - 1);
//		QuickSort(arr, pi + 1, r);
//	}
//}
//
//int FindSet(int parents[], int v) {
//	if (parents[v] != v) return FindSet(parents, parents[v]);
//	return v;
//}
//int kruskal() {
//	int vNum, eNum;
//	scanf("%d %d", &vNum, &eNum);
//	struct Edge_type* EdgeArr = (struct Edge_type*)malloc(sizeof(struct Edge_type) * eNum); //0���� �����ϱ�.
//	int* parents = (int*)malloc(sizeof(int) * (vNum + 1));
//
//
//	for (int i = 0; i < eNum; i++) {
//		int a, b, c;
//		scanf("%d %d %d", &a, &b, &c);
//		EdgeArr[i].u = a;
//		EdgeArr[i].v = b;
//		EdgeArr[i].cost = c;
//	}
//
//	QuickSort(EdgeArr, 0, eNum - 1);
//
//	for (int i = 0; i <= vNum; i++) //MakeSet
//		parents[i] = i;
//
//	int selectCnt = 0; //���õ� ���� ��
//	int sumCost = 0; //�ּҺ��
//
//	for (int i = 0; i < eNum; i++) {
//		int u = EdgeArr[i].u;
//		int v = EdgeArr[i].v;
//		int cost = EdgeArr[i].cost;
//
//		int root1 = FindSet(parents, u);
//		int root2 = FindSet(parents, v);
//
//		if (root1 == root2) continue;
//
//		if (root1 > root2) 
//			parents[root1] = root2;
//		else 
//			parents[root2] = root1; //unionFind�� ���� ���� ��Ȯ�� �ϱ�. ���⼭ parents�� ������ edge������ ���� ���ϳ�? 
//										  //���� ��� 1-2 �Ͽ� 1 root, 2-3�����ߴٸ� unionfind�ؼ� parents�� 1-3 ����� �� ������.
//
//		sumCost += cost;
//		if (++selectCnt >= vNum - 1)
//			break;
//	}
//	return sumCost;
//
//}
//
//int main(void) {
//	printf("%d", kruskal());
//	return 0;
//}