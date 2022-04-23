#include <iostream>
using namespace std;

void jednadzba(float a1, float b1, float c1, float a2, float b2, float c2)
{
    cout << a1 << "x + " << b1 << "y = " << c1 << endl;
    cout << a2 << "x + " << b2 << "y = " << c2 << endl;

    float x;
    x = (b1 * c2 - b2 * c1) / (b1 * a2 -a1 * b2);
    
    float y;
    y = (a1 * c2 - a2 * c1) / (a1 + b2 - a2 + b1);

    cout << "X je: " << x << endl;
    cout << "Y je: " << y << endl;
}

int main()
{
    jednadzba(3.0, 4.0, 8.0, -10.0, 7.0, 5.0);
    return 0;
}