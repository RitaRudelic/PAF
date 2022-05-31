#include <iostream>
#include <math.h>
#include "Particle.h"

Particle::Particle(double v, double theta, double x1, double y1, double step){
        

        x =  x1;
        y = y1;
        dt = step;
        
        float theta2;
        theta2= theta*3.14/180;
        
        
        vx = v*cos(theta2);
        vy = v*sin(theta2);

}

Particle::~Particle(){

}

void Particle::move(float dt){
    
        x = x + vx*dt;
        vy = vy + g*dt;
        y = y + vy*dt;
        t = t + dt;
        std::cout << y << std::endl;

}

double Particle::range(){
    
    do{
                move(dt);
                
            }
            while (y >= 0);

    std::cout << "Domet:" << std::endl;       
    std::cout << x << std::endl;
            
    return x;

}
        
double Particle::time(){

    do{
                move(dt);
            }
            while (y >= 0);
    
    std::cout << "Vrijeme:" << std::endl; 
    std::cout << t << std::endl;
            
    return t;
}


    
            