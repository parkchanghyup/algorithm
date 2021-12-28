#include<iostream>
#include<algorithm>

using namespace std;

class Student {
public : 
	string name;
	int score;

	Student(string name, int score) {
		this->name = name;
		this->score = score;
	}
	bool operator < (Student& student) {
		return this->score < student.score;
	}

};

int main() {
	Student students[] = {
		Student("나 동빈",90),
		Student("이 상욱",93),
		Student("박 한울",97),
		Student("강 종구",87),
		Student("이 태일",92)
	};

	sort(students, students + 5);
	for (int i = 0; i < 5; i++) {
		cout << students[i].name << endl;
	}
}