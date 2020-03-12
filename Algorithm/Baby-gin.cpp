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
//int Nums[6];
//int solve(int arr[], int pos, int used); //pos : 몇번째 숫자 선택 used : 어떤 숫자 사용?
//
//int main() {
//	int tcCnt;
//
//	cin >> tcCnt;
//	for (int t = 1; t <= tcCnt; ++t) 
//	{
//		for (int i = 0; i < 6; ++i)
//			cin >> Nums[i];
//
//		int arr[6]; //결과를 공통적으로 사용하기 위한 임시 변수  solve에서 pointer가 넘어가기 때문에.
//		cout << "#" << t << ' ' << solve(arr,0,0) << endl;  
//	}
//	return 0;
//}
//
//int solve(int arr[], int pos, int used) {
//	if (pos == 6) {
//		int tri = 0, run = 0;
//		for (int i = 0; i < 2; ++i) 
//		{
//			if (arr[i * 3 + 1] == arr[i * 3]+1 && arr[i * 3 + 2] == arr[i * 3 + 1]+1) // i = 0(앞 3개), arr[1] == arr[0]+1 and arr[2] == arr[1] + 1(차이 1)
//				++run;
//			else if (arr[i * 3 + 1] == arr[i * 3] && arr[i * 3 + 2] == arr[i * 3 + 1])
//				++tri;
//
//		}
//
//		if (run + tri == 2)
//			return 1;
//		return 0;
//	}
//
//	for (int i = 0; i < 6; ++i)
//	{
//		if (used & (1 << i)) continue;
//
//		arr[pos] = Nums[i];
//		if (solve(arr, pos + 1, used | (1 << i)))
//			return 1; //결과 값이 1이 나왔다면 1을 propagation(전파,보급,확산)해주는 역할 for 탐색 중도 baby-gin찾으면 종료가능.
//	}
//	return 0;
//}