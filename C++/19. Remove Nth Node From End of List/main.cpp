#include "solution.h"
#include <iostream>

using namespace std;

int main()
{
	Solution s;
//	NodeList1 = NodeList(0),
	ListNode* node_list = s.create(5);
	s.print(node_list);

	return 0;
}