
class BinarySearch
{
	public:
		int rank(int key, const int a[], int size)
		{
			int lo = 0;
			int hi = size -1;
			while (lo <= hi)
			{
				int mid = lo + (hi - lo)/2;
				if (key < a[mid]) hi = mid -1;
				else if (key > a[mid]) lo = mid + 1;
				else return mid;
			}
			return -1;
		}
};