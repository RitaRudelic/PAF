#include <iostream>
#include <HarmonicOscillator.h>


int main(){
    
    HarmonicOscillator h1(15, 0.2, 0.4, 0);
    h1.move(0.02,10);
    return 0;

}