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
//	if (pos == N) return -1; // 2개 미만 선택했을 경우. 최대값을 고르는 문제이므로 해가 될 수 없는 음의 값 반환.
//
//	int ret = 0, tmp;
//
//	tmp = solve(pos + 1, cnt + 1, val + Nums[pos]); //선택했을 경우
//	if (tmp > ret) ret = tmp;
//
//	tmp = solve(pos + 1, cnt, val); //선택 안했을 경우
//	if (tmp > ret) ret = tmp; //음수 
//
//	return ret;
//}