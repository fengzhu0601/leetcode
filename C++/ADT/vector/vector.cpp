#include "vector.h"
#include <iostream>

using namespace std;

template <typename T>
class MyPrint
{
    public:
        void operator()(T& e)
        {
            cout << e << " ";
        }
};

template <typename T>
class IncreaseElem{
    public:
        virtual void operator()(T& e)
        {
            e++;
        }
};

int main()
{
    cout << "hello world!!!" << endl;

    Vector<int> vec1(5);

    cout << vec1.size() << endl;
    cout << vec1.empty() <<endl;

    //Vector<int> vec2(vec1,5);
    //cout << vec2.size() << endl;
    //cout << vec2.empty() <<endl;

    vec1.insert(1);
    vec1.insert(2);
    vec1.insert(3);
    vec1.insert(4);
    vec1.insert(5);

    cout << vec1.size() << endl;
    cout << vec1.empty() <<endl;
    vec1.insert(3,7);
    cout << vec1.size() << endl;
    cout << vec1.empty() <<endl;

    MyPrint<int> visit;
    vec1.traverse(visit);
    cout << endl;

    IncreaseElem<int> increase_elem;
    vec1.traverse(increase_elem);
    vec1.traverse(visit);
    cout << endl;

    Vector<int> vec2(vec1,1,3);
    vec2.traverse(visit);
    cout << endl;


    return 0;
}

