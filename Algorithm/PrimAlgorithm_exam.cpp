//#define MAX_N 100
//#define INF 987654321
//int N, Graph[MAX_N][MAX_N], Parent[MAX_N], weight[MAX_N]; // N : number of Vertex   Parent: i -> childNode, value -> parentNode  weight : minweight from minVertex to idx(minVertex) to minParent
//int prim() { // start prim algorithm
//	for (int i = 0; i < N; ++i) // 0~N-1 vertex�� ����ġ -1�� �ʱ�ȭ.  -1�� ����x ����, 0�� ���� ��� ���� ��. �ʱⰪ, ���� ���� ����� ����. ����ġ
//		weight[i] = -1;
//	weight[0] = 0; //������ ������ 0������ ����.
//	for (int k = 1; k < N; ++k) { //n-2�� �ݺ��Ͽ� ��� ��� ����
//		int minWeight = INF, minVertex, minParent; //�� Tr(Ʈ��)�� ���� �ּ� ����ġ�� Ž���Ѵ�.
//		for (int i = 0; i < N; ++i) { //Ʈ���� ���� ��� ������ ���� Ž��
//			if (weight[i] < 0)  continue; //���þȵ� ����� �ƿ�! (������ ���þ��� ���´ϱ�.)
//			for (int j = 0; j < N; ++j) { //������ ��忡 ���Ͽ� 
//				if (weight[j] >= 0) continue; //Tr�� ���� ���� �ƿ�!
//				if (Graph[i][j] < minWeight) { //minVertex���� �۴ٸ� �ĺ������� ����.
//					minVertex = j; minParent = i; //��Ÿ �� ���.
//					minWeight = Graph[i][j];
//				}
//			}
//		}
//
//		Parent[minVertex] = minParent; weight[minVertex] = minWeight; //�ô� ��忡 ���� ����Ͽ� Tr�� ����
//	}
//	int sumCost = 0; //���� MST�� ���� ����ġ �ּҰ��� ����϶�.
//	for (int i = 0; i < N; ++i) sumCost += weight[i];
//	return sumCost;
//}
//int main(void) {
//	prim();
//	return 0;
//}
//
///*
//���д� Ʈ���� parents[]�� ���. idx = childNode, value = parentNode
//
//�׷����� ���� ������� ��� �Ǵ��ϴ°�? -> weight�� �̿��ؼ� �Ǵ�.  wieght�� �ܺ� ��尡 ���É��� �� ����ġ�� ���Ѵ�. �� MST_r���� �� �� vertex ���ý� �� ����ġ.
//weight�����δ� � vertex�� ����� edge���� �� �� ���� parents�� �̿��Ͽ� Ȯ���� �� ����.
//
//�θ��� -> �ڽĳ���� �����ϰ�
//
//
//
//*/