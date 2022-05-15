
using namespace std;
#include<vector>
#include<iostream>
#include<fstream>
#include<algorithm>

class HarmonicOscillator {

   private:

        double k, m, v, x;
        double a = -k*x/m;
        double t = 0;
    
    

    public:
    HarmonicOscillator(double k1, double m1, double x1, double v1);
    ~HarmonicOscillator();

    vector<double>xl;
    vector<double>vl;
    vector<double>al;
    vector<double>tl;

    void move(float dt, float t1);
};
