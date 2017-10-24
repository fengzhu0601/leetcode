#include <iostream>
#include "./vector/Vector.h"
#include "speak.h"

using namespace std;

int main()
{
    cout << "hello world!!!" << endl;

    Vector<int> vec1(5);

    cout << vec1.size() << endl;
    cout << vec1.empty() <<endl;

    vec1.insert(1);
    vec1.insert(0,1);

    Speak speak;
    speak.sayHello("world");

    // vec1.insert(0,2);
    // vec1.insert(0,3);
    // vec1.insert(0,4);
    // vec1.insert(0,5);

    return 0;
}