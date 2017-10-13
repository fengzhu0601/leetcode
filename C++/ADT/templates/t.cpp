#include "t.h"

template <typename T>
A<T>::A(){}

template <typename T>
T A<T>::g(T a, T b)
{
    return a+b;
}

