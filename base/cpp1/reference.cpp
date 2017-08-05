#include <iostream>
using namespace std;

int main()
{
	double d = 123.45;
	double& e = d;//e是d的别名，两者是同一个变量
	//double*const E=&d;后面的e都相当于*E
	//double& f = 123.45;//引用只能用变量来初始化
	const double& c = 234.56;
	const double& s = d+5;
	cout << "&d=" << &d << ", &e=" << &e << endl;
	//int& n = d;//类型不一致
	cout << "d=" << d << ",e=" << e << "c=" << c << "s=" << s << endl;
	double& e2 = e;
	cout << "&e2=" << &e2 << ", e2=" << e2 << endl;
	e2 = 78.9;
	cout << "d=" << d << ", e=" << e << endl;
}

/*
&d=0x7ffeab152500, &e=0x7ffeab152500
d=123.45,e=123.45c=234.56s=128.45
&e2=0x7ffeab152500, e2=123.45
d=78.9, e=78.9
*/
