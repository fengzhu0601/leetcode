#include <climits>

class solution
{
public:
	int reverse(int x)
	{
		int r = 0;
		int n;
		while (x != 0)
		{
			n = x % 10;

			if (r > INT_MAX / 10 || r < INT_MIN / 10)
				return 0;
			r = r * 10 + n;
			x /= 10;
		}
		return r;
	}
};