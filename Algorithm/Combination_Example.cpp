//#include <iostream>
//#include <stdio.h>
//using namespace std;
//
//#define MAX_N 10
////input
////2
////4
////1 2 3 4
////5
////2 1 3 5 4
//int N, Nums[MAX_N];
//
//int solve(int pos, int cnt, int val);
//
//int main() {
//	int tcCnt;
//
//	cin >> tcCnt;
//
//	for (int t = 1; t <= tcCnt; ++t) {
//		cin >> N;
//		for (int i = 0; i < N; ++i)
//			cin >> Nums[i];
//
//		cout << "#" << t << ' ' << solve(0, 0, 0) << endl;
//	}
//	return 0;
//}
//
//int solve(int pos, int cnt, int val) {
//	if (cnt == 2) return val;
//	if (pos == N) return -1; // 2�� �̸� �������� ���. �ִ밪�� ���� �����̹Ƿ� �ذ� �� �� ���� ���� �� ��ȯ.
//
//	int ret = 0, tmp;
//
//	tmp = solve(pos + 1, cnt + 1, val + Nums[pos]); //�������� ���
//	if (tmp > ret) ret = tmp;
//
//	tmp = solve(pos + 1, cnt, val); //���� ������ ���
//	if (tmp > ret) ret = tmp; //���� 
//
//	return ret;
//}