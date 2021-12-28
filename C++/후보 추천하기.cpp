#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int recommend[101];

int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(0);

	int N, M;
	cin >> N >> M;

	//순서 , 사진
	vector<pair<int, int>> v(N);


	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;
		recommend[num]++;

		bool change = true;
		for (int j = 0; j < N; j++) {

			//사진틀이 비어있는 경우

			if (v[j].second == 0) {
				v[j].second = num;
				v[j].first = i;
				change = false;
				break;
			}

			//이미 후보자의 사진이 등록되 있는 경우

			else if (v[j].second == num) {
				change = false;
				break;
			}

		}

		//사진틀이 비어있지않고 사진틀에 후보자의 사진이 없을경우

		if (change) {

			int idx = 0;

			for (int j = 1; j < N; j++) {

				//제일 추천 수가 낮은 사진들이 여러개인 경우
				if (recommend[v[j].second] == recommend[v[idx].second]) {

					//먼저 등록된 
					if (v[j].first < v[idx].first) idx = j;

				}

				//추천수가 낮은 순서로
				else if (recommend[v[j].second] < recommend[v[idx].second]) {
					idx = j;
				}
			}

			recommend[v[idx].second] = 0; //바꿔쳐지면 추천수 초기화

			v[idx].first = i;
			v[idx].second = num;

		}
	}

	vector<int> picture;

	for (int i = 0; i < N; i++) {
		picture.push_back(v[i].second);
	}

	sort(picture.begin(), picture.end());
	for (int i = 0; i < N; i++)cout << picture[i] << " ";
}