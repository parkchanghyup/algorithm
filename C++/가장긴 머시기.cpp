#include <string>
#include<iostream>
using namespace std;

int longest = 1;
string word; int wordsize;

void oddlengthCheck(int position) { //홀수 길이의 팰린드롬이라 가정했을때 길이 구하기
	int count = 1;
	for (int i = 1; i <= wordsize; i++) {
		if ((position - i < 0) || (position + i >= wordsize))
			break;
		if (word[position - i] == word[position + i])
			count += 2;
		else
			break;
	}
	if (count > longest)
		longest = count;
}
void evenlengthCheck(int position) { //짝수 길이의 팰린드롬이라 가정했을때 길이 구하기
	int count = 0;
	for (int i = 0; i < wordsize; i++) {
		if ((position - i < 0) || (position + i >= wordsize - 1))
			break;
		if (word[position - i] == word[position + i + 1])
			count += 2;
		else
			break;
	}
	if (count > longest)
		longest = count;
}

void solution(string s)
{

	word = s;
	wordsize = s.length();
	for (int i = 0; i < s.length(); i++) {
		oddlengthCheck(i);
		evenlengthCheck(i);
	}
	return;
}

int main() {
	string a[101];
	for (int i = 0; i < 100; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < 100; i++) {
		solution(a[i]);
	}

	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			if (i < j)
			{
				char t = a[i][j];
				a[i][j] = a[j][i];
				a[j][i] = t;
			}

	for (int i = 0; i < 100; i++) {
		solution(a[i]);
	}
	cout << longest;
}