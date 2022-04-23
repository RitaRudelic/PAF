#include <iostream>

void kruznica (float x1, float y1, float x2, float y2, float r) {
    
    float a;
    a = (x1, y1);

    float b;
    b = (x2,y2);

    float d;
    d = (a-b);

    if (d > r) {
        std::cout<<"Točka je izvan kružnice."<<std::endl;
    }
    
    else if (d < r) {
        std::cout<<"Točka je unutar kružnice."<<std::endl;
    }
    else {
        std::cout<<"Točka je na kružnici."
    }    

}

int main() {
    kruznica(3, 4, 5, 6, 3);
    
    return 0;
}