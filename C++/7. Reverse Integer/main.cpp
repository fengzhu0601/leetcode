#include "solution.h"
#include <iostream>

int main()
{
	solution s;
	std::cout << s.reverse(123) << std::endl;
	std::cout << s.reverse(-123) << std::endl;
	std::cout << s.reverse(125384977) << std::endl;
	std::cout << s.reverse(-125384977) << std::endl;

	return 0;
}