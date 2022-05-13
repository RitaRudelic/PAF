class HarmonicOscillator {

   private:

        double k, m, v, x;
        double a = -k*x/m;
        double t = 0;
    
    

    public:
    HarmonicOscillator(double k1, double m1, double x1, double v1);
    ~HarmonicOscillator();

    void move(float dt, float t1);
};
