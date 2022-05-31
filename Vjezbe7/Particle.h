class Particle {

    private:

    double t, x, y, vx, vy;
    float dt;
    double g = -9.81;
    void move(float dt);

    public:
    Particle(double v, double theta, double x0, double y0, double step = 0.001);
    ~Particle();

    double range();
    double time();

};

