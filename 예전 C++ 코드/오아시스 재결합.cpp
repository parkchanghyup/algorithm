#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;

int main(void)

{

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;

	stack<pair<int, int>> s; //키, 연속 몇 명

	ll result = 0;

	for (int i = 0; i < N; i++)
	{
		int h;
		cin >> h;

		//현재 사람의 키가 스택의 top에 있는 사람보다 크다면

		while (!s.empty() && s.top().first < h)
		{
			result += s.top().second;
			s.pop();
		}

		if (s.empty())
			s.push({ h, 1 });

		else {
			//같은 키의 경우 따로 처리

			if (s.top().first == h) {
				pair<int, int> cur = s.top();
				s.pop();
				result += cur.second;
				//스택 내 제일 큰 사람과 쌍을 이룸
				if (!s.empty())
					result++;

				//연속해서 같은 키가 나오므로
				cur.second++;
				s.push(cur);
			}

			//더 작은 사람이 왔을 경우

			else
			{
				s.push({ h, 1 });
				result++;
			}
		}
	}
	cout << result << "\n";

	return 0;

}