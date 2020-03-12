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
//int solve(); //input을 gloval value로 들고 있기 때문에 input val 필요없음.
//
//int main() {
//	int tcCnt;
//
//	cin >> tcCnt;
//	for (int t = 1; t <= tcCnt; ++t) {
//		cin >> N;
//		for (int i = 0; i < N; ++i)
//			cin >> Nums[i];
//
//		cout << "#" << t << ' ' << solve() << endl;
//	}
//	return 0;
//}
//
//
//int countBits(int value) {
//	int count = 0;
//	while (value > 0) {
//		if ((value & 1) == 1)
//			count++;
//		value = value >> 1;
//	}
//	return count;
//}
//
//int solve() {
//	int ret = 0;
//	for (int i = 0; i < (1 << N); ++i) { //N개의 원소를 갖는 부분 집합의 수. 1<<N 즉, 가질 수 있는 부분 집합의 수 만큼 반복.
//		if (countBits(i) == 2) {
//			int sum = 0;
//			for (int j = 0; j < N; ++j) {
//				if (i & (1 << j))
//					sum += Nums[j];
//			}
//			if (sum > ret) ret = sum;
//		}
//	}
//
//	return ret;
//}