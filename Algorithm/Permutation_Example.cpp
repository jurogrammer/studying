//#include <iostream>
//#include <stdio.h>
//using namespace std;
//// input
//// 2
//// 4
//// 1 2 3 4
//// 5
//// 2 1 3 5 4��
//
//#define MAX_N 10
//
//int N, Nums[MAX_N];
//int solve(int cnt, int used, int val);
//
//int main(void) 
//{	
//	int tcCnt;
//	//freopen("numbers_input.txt", "r", stdin);
//
//	cin >> tcCnt;
//	for (int t = 1; t <= tcCnt; ++t) {
//		cin >> N;
//		for (int i = 0; i < N; ++i)
//			cin >> Nums[i];
//		cout << "#" << t << ' ' << solve(0, 0, 0) << endl;
//	}
//	return 0;
//}
//
//int solve(int cnt, int used, int val) { //cnt � ���� ���� used : � ���� �����ߴ���(�ߺ������ƴ�) val : 
//	if (cnt == 2)
//		return val;
//
//	int ret = 0; //�� ���ÿ� ���ؼ� ret�� �����ϴϱ�...!! global ���� ���ص� �ִ밪 ���� �� ����.
//	for (int i = 0; i < N; ++i) {
//		if (used & (1 << i)) continue; //��� ��� �� Ȯ��.
//
//		int tmp = solve(cnt + 1, used | (1 << i), val * 10 + Nums[i]);  // val*10�� �ڸ� �� �÷��ִ� ��. �������� << ����� ���
//		if (tmp > ret)
//			ret = tmp;
//	}
//	return ret;
//}