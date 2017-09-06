#include<iostream>
#include "List.h"

using namespace std;

int main() {
	List l;
	l.push_front(5);//5
	l.push_front(8);//8 5
	l.push_front(20);//20 8 5
	l.travel();
	l.insert(9,2);//20 8 9 5
	l.insert(6,100);//6 20 8 9 5
	l.insert(7,-10);//7 6 20 8 9 5
	l.insert(1,2);//7 6 1 20 8 9 5
	l.travel();
	l.push_back(10).push_back(15).travel();

	l.erase(0);//x7:6 1 20 8 9 5 10 15
	l.erase(l.size()-1);//x15:6 1 20 8 9 5 10
	l.erase(2);//x20:6 1 8 9 5 10
	l.travel();

}