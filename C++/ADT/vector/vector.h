#include<stdlib.h>

typedef int Rank;
#define DEFAULT_CAPACITY 3

template <typename T>   //元素类型

class Vector{
private:
	Rank _size;
	int _capacity;
	T* _elem;

protected:
	void copyFrom(T* const A, Rank lo, Rank hi);    //复制数组区间A[lo,hi]
	void expand();                                  // 空间不足时扩容
	void shrink();                                  // 填装因子过小时压缩
	bool bubble(Rank lo, Rank hi);                  // 扫描交换算法
	void bubbleSort(Rank lo, Rank hi);              // 起泡排序算法
	void merge(Rank lo, Rank mi, Rank hi);          // 归并算法
	void mergeSort(Rank lo, Rank hi);               // 归并排序算法
	Rank partition(Rank lo, Rank hi);               // 轴点构造算法
	void quickSort(Rank lo, Rank hi);               // 快速排序算法
	void heapSort(Rank lo, Rank hi);                // 堆排序

public:
	// 构造函数
	Vector(int c = DEFAULT_CAPACITY) //默认
	{
		_elem = new T[_capacity = c];
		_size = 0;
	}

	Vector(T* A, Rank lo, Rank hi)//数组区间复制
	{
		copyFrom(A, lo, hi);
	}

	Vector(T* A, Rank n)//数组整体复制
	{
		copyFrom(A, 0, n);
	}

	Vector(Vector<T> const& V, Rank lo, Rank hi)//向量区间复制
	{
		copyFrom(V._elem, lo, hi);
	}

	Vector(Vector<T> const& V, Rank n)//向量整体复制
	{
		copyFrom(V._elem, 0, V._size);
	}
	// 析构函数
	~Vector()
	{
		delete[] _elem;
	}

	//只读访问接口
	Rank size() const   //规模
	{
		return _size;
	}

	bool empty() const  //判空
	{
		return  _size<= 0;
	}

	int disordered() const; //判断向量是否已排序
	Rank find(T const& e) const     //无序向量整体查找
	{
		return find(e, 0, (Rank)_size);
	}
	Rank find(T const& e, Rank lo, Rank hi) const;  //无序向量区间查找

	Rank search(T const& e) const  //有序向量整体查找
	{
		return (0 >= _size) ? -1 : search(e, (Rank)0, (Rank)_size);
	}
	Rank search(T const& e, Rank lo, Rank hi) const; //有序向量区间查找

	// 可写访问接口
	T& operator[](Rank r) const;    //重载下标操作符， 可以类似于数组形式引用各元素
	Vector<T>& operator=(Vector<T> const&); //重载赋值操作符，以便直接克隆向量
	T remove(Rank r);   //删除秩为r的元素
	int remove(Rank lo, Rank hi); // 删除秩在区间lo,hi之内的元素
	Rank insert(Rank r, T const& e); // 插入元素
	Rank insert(T const& e) //默认作为末元素插入
	{
		return insert(_size, e);
	}
	void sort(Rank lo, Rank hi); // 对lo,hi排序
	void sort() //整体排序
	{
		sort(0,_size);
	}
	void unsort(Rank lo, Rank hi); //对lo,hi置乱
	void unsort()   //整体置乱
	{
		unsort(0, _size);
	}

	int deduplicate();  //无序去重
	int uniquify();     //有序去重

	//遍历
	void traverse(void(*)(T&)); //遍历(使用函数指针，只读或局部性修改)
	template<typename VST> void traverse(VST&); //遍历（使用函数对象，可全局性修改）
};


template <typename T>
void Vector<T>::copyFrom(T* const A, Rank lo, Rank hi)
{
	_elem = new T[_capacity = 2*(hi - lo)];
	_size = 0;
	while(lo < hi)
		_elem[_size++] = A[lo++];
}

// 重载=运算符
template < typename T>
Vector<T>& Vector<T>::operator=(Vector<T> const& V)
{
    int n = V.size();
    if(_capacity < n)
    {
        delete [] _elem;
        _elem = new T[_capacity = 2*n];
        copyFrom(V._elem, 0, n);
        return *this;
    }
}

//扩容
template <typename T>
void Vector<T>::expand()
{
    if(_size < _capacity) return;
    if(_capacity < DEFAULT_CAPACITY) _capacity = DEFAULT_CAPACITY;

    T* oldElem = _elem;
    _elem = new T[_capacity <<= 1];
    for(int i= 0; i<_size;i++)
        _elem[i] = oldElem[i];
    delete [] oldElem;

}

//缩容
template <typename T>
void Vector<T>::shrink()
{
    if(_capacity < DEFAULT_CAPACITY << 1) return;
    if(_size << 2 > _capacity) return;
    T* oldElem = _elem;
    _elem = new T[_capacity >>= 1];
    for(int i=0; i<_size; i++)
        _elem[i] = oldElem[i];
    delete [] oldElem;
}

//重载向量操作符[]
template <typename T>
T& Vector<T>::operator[](Rank r) const
{
    return _elem[r];
}

//置乱器
//template <typename T>
//void premute(Vector<T>& V)
//{
//    for(int i=V.size(); i>0; i--)
//        swap(V[i-1], V[rand() % i]);
//}


template <typename T>
void Vector<T>::unsort(Rank lo, Rank hi)
{
    T* V = _elem + lo;
    for(Rank i=hi -lo; i> 0; i--)
        swap(V[i-1],V[rand() % i]);
}

//判等器
template <typename T> static bool lt(T* a, T* b) { return lt(*a, *b); }
template <typename T> static bool lt(T& a, T& b) { return a < b; }
template <typename T> static bool eq(T* a, T* b) { return eq(*a, *b); }
template <typename T> static bool eq(T& a, T& b) { return a == b; }

//查找
template <typename T>
Rank Vector<T>::find(T const& e, Rank lo, Rank hi) const
{
    while((lo < hi--) && (_elem[hi] != e));

    return hi;
}

// 插入
template <typename T>
Rank Vector<T>::insert(Rank r, T const& e)
{
    expand();
    for( int i=_size; i> r; i-- )
        _elem[i] = _elem[i-1];
    _elem[r] = e;
    _size++;
    return r;
}

//删除
template <typename T>
int Vector<T>::remove(Rank lo, Rank hi)
{
    if(lo == hi) return 0;
    while(hi < _size)
        _elem[lo++] = _elem[hi++];
    _size = lo;
    shrink();
    return hi -lo;
}
//删除单个元素
template <typename T>
T Vector<T>::remove(Rank r)
{
    T e = _elem[r];
    remove(r, r+1);
    return e;
}


//无序去重复
template <typename T>
int Vector<T>::deduplicate()
{
    int oldSize = _size;
    Rank i=1;
    while(i < _size)
        (0>find(_elem[i],0,i))?i++: remove(i);
    return oldSize - _size;
}


//遍历向量，对各节点依次实施visit操作
template <typename T>
void Vector<T>::traverse(void (*visit)(T&))
{
    for(int i=0; i < _size; i++)
        visit(_elem[i]);
}

template <typename T>
template <typename VST>
void Vector<T>::traverse(VST& visit)
{
    for(int i=0; i < _size; i++)
        visit(_elem[i]);
}
