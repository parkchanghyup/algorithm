#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int INF = 987654321;
int cacheThree[61][61][61];

int scvThree(int a, int b, int c)
{
	// 음수가 나올시에는 0으로 바꿔준다.
	if (a < 0) return scvThree(0, b, c);
	if (b < 0) return scvThree(a, 0, c);
	if (c < 0) return scvThree(a, b, 0);

	if (a == 0 && b == 0 && c == 0)
		return 0;

	int ret = cacheThree[a][b][c];
	if (ret != -1)
		return ret;

	ret = INF;
	ret = min(ret, scvThree(a - 9, b - 3, c - 1) + 1);
	ret = min(ret, scvThree(a - 9, b - 1, c - 3) + 1);

	ret = min(ret, scvThree(a - 1, b - 3, c - 9) + 1);
	ret = min(ret, scvThree(a - 1, b - 9, c - 3) + 1);

	ret = min(ret, scvThree(a - 3, b - 1, c - 9) + 1);
	ret = min(ret, scvThree(a - 3, b - 9, c - 1) + 1);

	return ret;

}
int main()
{
	int N;
	cin >> N;
	int cand[3] = { 0,0,0 };
	int ans;

	for (int i = 0; i < N; ++i)
		cin >> cand[i];

	memset(cacheThree, -1, sizeof(cacheThree));
	ans = scvThree(cand[0], cand[1], cand[2]);

	cout << ans << "\n";
	return 0;
}