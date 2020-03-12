//#define MAX_N 100
//#define INF 987654321
//int N, Graph[MAX_N][MAX_N], Parent[MAX_N], weight[MAX_N]; // N : number of Vertex   Parent: i -> childNode, value -> parentNode  weight : minweight from minVertex to idx(minVertex) to minParent
//int prim() { // start prim algorithm
//	for (int i = 0; i < N; ++i) // 0~N-1 vertex의 가중치 -1로 초기화.  -1은 연결x 상태, 0은 본인 노드 향한 것. 초기값, 양의 값은 연결된 상태. 가중치
//		weight[i] = -1;
//	weight[0] = 0; //임의의 정점인 0번부터 시작.
//	for (int k = 1; k < N; ++k) { //n-2번 반복하여 모든 노드 연결
//		int minWeight = INF, minVertex, minParent; //현 Tr(트리)에 대해 최소 가중치를 탐색한다.
//		for (int i = 0; i < N; ++i) { //트리에 속한 노드 각각에 대해 탐색
//			if (weight[i] < 0)  continue; //선택안된 노드라면 아웃! (음수면 선택안한 상태니까.)
//			for (int j = 0; j < N; ++j) { //선택한 노드에 대하여 
//				if (weight[j] >= 0) continue; //Tr에 속한 노드면 아웃!
//				if (Graph[i][j] < minWeight) { //minVertex보다 작다면 후보군으로 선택.
//					minVertex = j; minParent = i; //기타 값 기록.
//					minWeight = Graph[i][j];
//				}
//			}
//		}
//
//		Parent[minVertex] = minParent; weight[minVertex] = minWeight; //봤던 노드에 대해 기록하여 Tr로 갱신
//	}
//	int sumCost = 0; //구한 MST에 대해 가중치 최소값을 계산하라.
//	for (int i = 0; i < N; ++i) sumCost += weight[i];
//	return sumCost;
//}
//int main(void) {
//	prim();
//	return 0;
//}
//
///*
//스패닝 트리를 parents[]로 기록. idx = childNode, value = parentNode
//
//그래프에 속한 노드인지 어떻게 판단하는가? -> weight를 이용해서 판단.  wieght는 외부 노드가 선택됬을 때 가중치를 말한다. 즉 MST_r에서 그 외 vertex 선택시 그 가중치.
//weight만으로는 어떤 vertex와 연결된 edge인지 알 수 없고 parents를 이용하여 확인할 수 있음.
//
//부모노드 -> 자식노드라고 생각하고
//
//
//
//*/