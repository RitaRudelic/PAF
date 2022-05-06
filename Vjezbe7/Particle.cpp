#include <iostream>
#include <math.h>
#include "Particle.h"

Particle::Particle(double v, double theta, double x1, double y1, double step){
        

        x =  x1;
        y = y1;
        
        float theta2;
        theta2= theta*3.14/180;
        
        
        vx = v*cos(theta2);
        vy = v*sin(theta2);

}

Particle::~Particle(){

}

void Particle::move(float dt){
    
        x = x + vx*dt;
        vy = vy - g*dt;
        y = y + vy*dt;
        t = t + dt;

}

double Particle::range(){
    
    do{
                move(dt);
            }
            while (y1 >= 0);
           
            

            std::cout << x << std::endl;

}
        
double Particle::time(){

    do{
                move(dt);
            }
            while (y1 >= 0);
            
            std::cout << t << std::endl;
}


    
            