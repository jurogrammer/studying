//#include <iostream>
//#include <stdio.h>
//using namespace std;
//#define INF 987654321
//#define MAX_N 6
//int N, Graph[MAX_N][MAX_N];
//int solve(int pos, int visited);
//int Solution(void)
//{   
//    int tcCnt;
//    freopen("tsp_input.txt", "r", stdin);
//    cin >> tcCnt;
//    for (int t = 1; t <= tcCnt; ++t) {
//        cin >> N;
//        for (int i = 0; i <N; ++i)
//            for (int j = 0; j<N; ++j)
//                cin >> Graph[i][j];
//
//        int ans = INF;
//        for (int i = 0; i < N; ++i) {
//            int tmp = solve(1, 1 << i);
//            if (ans > tmp) ans = tmp;
//        }
//        cout << "#" << t << ' ' << ans << endl;
//    }
//    return 0;
//}
//
//int solve(int pos, int visited)
//{
//    if (visited == (1 << N) - 1)
//        return 0;
//
//    int ret = INF;
//    for (int next = 0; next < N; ++next)
//    {
//        if (!(visited & (1 << next)) && Graph[pos][next])
//        {
//            int tmp = Graph[pos][next] + solve(next, visited | (1 << next));
//            if (tmp < ret)
//                ret = tmp;
//        }
//    }
//    return ret;
//}