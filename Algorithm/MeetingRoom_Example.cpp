//#include <iostream>
//#include <stdio.h>
//using namespace std;
//
////input
////10
////1 4 1 6 6 10 5 7 3 8 5 9 3 5 8 11 2 13 12 14
//
//struct meeting_type { 
//	int start;
//	int end;
//};
//
//int N;
//meeting_type Meetings[10];
//
//int solve();
//
//int main() {
//
//	cin >> N;
//	for (int i = 0; i < N; ++i)
//		cin >> Meetings[i].start >> Meetings[i].end;
//
//	cout << solve() << endl;
//
//	return 0;
//}
//
//int solve() {
//	for (int i = 0; i < N - 1; ++i) { //sorting ´Ü¼øÈ­.
//		for (int j = i + 1; j < N; ++j) {
//			if (Meetings[i].end > Meetings[j].end) {
//				meeting_type tmp = Meetings[i];
//				Meetings[i] = Meetings[j];
//				Meetings[j] = tmp;
//			}
//		}
//	}
//
//	int lastEnd = 0, cnt = 0;
//	for (int i = 0; i < N; ++i) {
//		if (Meetings[i].start < lastEnd) continue;
//
//		printf("(%d,%d)\n", Meetings[i].start, Meetings[i].end);
//		lastEnd = Meetings[i].end;
//		++cnt;
//	}
//	return cnt;
//}