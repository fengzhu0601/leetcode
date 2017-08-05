#include <iostream>
using namespace std;

int main()
{
	bool gender = true;
	bool sex = false;
	cout << (gender?"帅哥":"美女") << endl;
	cout << (sex?"男":"女") << endl;
	cout << gender << ',' << sex << endl;
	cout << boolalpha << gender << ',' << sex << endl;
}

/*
 fengzhu@ubuntu  ~/fengzhu/leetcode/base/cpp1   master ●✚  g++ bool.cpp
 fengzhu@ubuntu  ~/fengzhu/leetcode/base/cpp1   master ●✚  ./a.out
帅哥
女
1,0
true,false
*/

