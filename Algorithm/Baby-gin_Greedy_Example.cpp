//#include <iostream>
//#include <stdio.h>
//using namespace std;
//
////input
////4
////1 2 4 7 8 3
////6 6 7 7 6 7
////0 5 4 0 6 0
////1 0 1 1 2 3
//int Nums[6], Cnt[10];
//int solve(); //pos : 몇번째 숫자 선택 used : 어떤 숫자 사용?
//
//int main() {
//	int tcCnt;
//
//	cin >> tcCnt;
//	for (int t = 1; t <= tcCnt; ++t) 
//	{
//		for (int i = 0; i < 10; ++i)
//			Cnt[i] = 0;
//
//		for (int i = 0; i < 6; i++) {
//			cin >> Nums[i];
//			Cnt[Nums[i]]++;
//		}
//
//		cout << "#" << t << ' ' << solve() << endl;  
//	}
//	return 0;
//}
//
//int solve()
//{
//	int tri = 0, run = 0;
//	for (int i = 0; i < 10; ) {
//		if (Cnt[i] >= 3) {
//			Cnt[i] -= 3;
//			tri++;
//		}
//		else if (i <= 7 && Cnt[i] >= 1 && Cnt[i + 1] >= 1 && Cnt[i + 2] >= 1) {
//			Cnt[i]--;
//			Cnt[i + 1]--;
//			Cnt[i + 2]--;
//			run++;
//		}
//		else {
//			++i;
//		}
//	}
//
//	if (tri + run == 2)
//		return 1;
//
//	return 0;
//}
