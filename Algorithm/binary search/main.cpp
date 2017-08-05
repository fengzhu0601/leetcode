#include "binary_search.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	BinarySearch b;
	int j[] = {1,2,3,4,5,7,9,2,9};
	int size = sizeof(j) / sizeof(j[0]);
	cout << b.rank(9, j, size) << endl;
	return 0;
}
