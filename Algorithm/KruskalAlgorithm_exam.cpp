///*
//Kruskal Algorithm!
//
//Edge를 오름차순 정렬
//edge가 가장 작은 값부터 선택해서 MST 생성. -> n-1반복하여 edge생성 해야함.
//
//edge는 struct로 표현. u,v,weight
//
//parents 변수를 통해 싸이클여부 판단
//
//싸이클 판단법
//u와 v가 같은 노드이면 제외.
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
//	/* 다 계산해도 i는 현재 가장 작은 위치를 나타냄. 그래서 1증가 시킨 값과 pivot을 교환하여 pivot이 딱 가르도록 만들어줌. */
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
//	struct Edge_type* EdgeArr = (struct Edge_type*)malloc(sizeof(struct Edge_type) * eNum); //0번은 없으니까.
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
//	int selectCnt = 0; //선택된 엣지 수
//	int sumCost = 0; //최소비용
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
//			parents[root2] = root1; //unionFind로 추후 관계 명확히 하기. 여기서 parents는 선택한 edge정보를 담지 못하네? 
//										  //예를 들어 1-2 하여 1 root, 2-3선택했다면 unionfind해서 parents에 1-3 연결될 수 있으니.
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