#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

void poljecijelihbrojeva(int lista[], int a, int b)
{
    for(int i=a; i<b; i++)
    {
        cout << lista[i] << " " ;
    }
    cout << "\n";
}

void zamjenadvael(int lista[], int a, int b)
{
    swap(lista[a], lista[b]);
    for(int i=0; i<7; i++)
    {
        cout << lista[i] << " " ;
    }
    cout << "\n";
}

void zamjenael(int lista[], int N)
{
    int skupljac[N];
    for(int i=N-1; i>=0; i--)
    {
        skupljac[N-1 - i] = lista[i] ;
    }
    for(int i=0; i<N-1; i++)
    {
        cout << skupljac[i] << " " ;
    }
    cout << "\n";
}

int main()
{
    int lista[7] = {2,3,4,5,6,7,8};
    
    poljecijelihbrojeva(lista, 2, 7);
    
    zamjenadvael(lista, 4, 6);
    
    zamjenael(lista, 4);

    return 0;
}