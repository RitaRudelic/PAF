#include <iostream>

void jednadzba(float x1, float y1, float x2, float y2) {
    float k; 
    k = (y2-y1)/(x2-x1);
    float l;
    l = k*(-x1) + y1;

    if (l == 0){
        std::cout<<"y="<< k << "x"<<std::endl;
        }
    else {
        std::cout<<"y="<< k << "x+" << l <<std::endl;
    }
}      

int main() {
    jednadzba(2,3,4,4);
    
    return 0;
}
