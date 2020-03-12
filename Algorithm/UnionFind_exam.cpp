//#include <stdio.h>
//
//int Parent[5] = { 0, };
//
//void MakeSet(int v) {
//	Parent[v] = -1;
//};
//
//int FindSet(int v) {
//	if (Parent[v]<0) return v;
//	return FindSet(Parent[v]);
//};
//
//void UnionSet(int u, int v) {
//	int root1 = FindSet(u);
//	int root2 = FindSet(v);
//	if (root1 == root2) return;
//
//	Parent[root1] += Parent[root2];
//	Parent[root2] = root1;
//};
//
//int main(void) {
//	for (int i = 0; i < sizeof(Parent) / sizeof(Parent[0]); i++)
//	{
//		MakeSet(i);
//		printf("%d\n", Parent[i]);
//	}
//
//	UnionSet(0, 1);
//	UnionSet(1, 2);
//	UnionSet(2, 3);
//	
//	for (int i = 0; i < 5; i++)
//		printf("Parent[%d]\n ", Parent[i]);
//
//
//}