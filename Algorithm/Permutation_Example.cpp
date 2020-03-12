//#include <iostream>
//#include <stdio.h>
//using namespace std;
//// input
//// 2
//// 4
//// 1 2 3 4
//// 5
//// 2 1 3 5 4ㅡ
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
//int solve(int cnt, int used, int val) { //cnt 몇개 숫자 선택 used : 어떤 숫자 선택했는지(중복순열아님) val : 
//	if (cnt == 2)
//		return val;
//
//	int ret = 0; //이 스택에 대해선 ret을 공유하니깐...!! global 선언 안해도 최대값 구할 수 있음.
//	for (int i = 0; i < N; ++i) {
//		if (used & (1 << i)) continue; //사용 됬는 지 확인.
//
//		int tmp = solve(cnt + 1, used | (1 << i), val * 10 + Nums[i]);  // val*10은 자리 수 올려주는 것. 이진수의 << 연산과 비슷
//		if (tmp > ret)
//			ret = tmp;
//	}
//	return ret;
//}