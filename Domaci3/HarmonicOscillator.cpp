#include <iostream>
#include <math.h>
#include "HarmonicOscillator.h"

HarmonicOscillator::HarmonicOscillator(double k1, double m1, double x1, double v1){
        
        k = k1;
        m = m1;
        x = x1;
        v = v1;

}

HarmonicOscillator::~HarmonicOscillator(){

}

void HarmonicOscillator::move(float dt, float t1){
    
        int N = int(t1/dt);

        for (int i = 0; i < N; i++){
                
                a = -k*x/m;
                v = v + a*dt;
                x = x + v*dt;
                t = t + dt;
                
                xl.push_back(x);
                vl.push_back(v);
                al.push_back(a); 
                tl.push_back(t);

                std::cout << x << std::endl;
            }



}


    
            