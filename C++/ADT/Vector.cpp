#include<Vector.h>
#include<stdlib.h>

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
