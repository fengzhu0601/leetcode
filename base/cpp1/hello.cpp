#include <iostream>//input/output stream
#include <string>
using namespace std;
int main()
{
	cout << "请输入您的姓名和年龄:\n";
	string name;
	int age;
	cin >> name >> age;
	cout << name << "您好，您出生于" << 2010-age << "年"
		<< endl;//end line==>'\n'
//	return 0;//main函数末尾的return 0可有可无
}

