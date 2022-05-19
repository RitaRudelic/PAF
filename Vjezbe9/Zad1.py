import math
import matplotlib.pyplot as plt

class BJ:
    
    def __init__(self, k, m, v0, h0, l, rho=1.125, Cd=1, A=1, dt=0.001, otpor_z = True):
        
        self.k = k 
        self.m = m
        self.l = l
        self.h0 = h0
        self.rho = rho 
        self.Cd = Cd
        self.A = A
        self.dt = dt
        self.otpor_z = otpor_z
        self.h = h0
        self.v0 = 0 
        self.t = 0 
        
        self.h1 = []
        self.t1 = []
        
        self.h1.append(self.h)
        self.t1.append(self.t)
        
        self.U = self.m * 9.81 * self.h
        self.K = 0 
        self.Ee = 0
        self.E = self.U + self.K + self.Ee
        
        self.U1= []
        self.K1 = []
        self.Ee1 = []
        self.E1 = []
        
        self.U1.append(self.U)
        self.K1.append(self.K)
        self.Ee1.append(self.Ee)
        self.E1.append(self.E)

    def reset(self):
        
        del self.k 
        del self.m
        del self.l
        del self.h0
        del self.rho
        del self.Cd
        del self.A
        del self.dt
        del self.otpor_z
        del self.h
        del self.v0
        del self.t 
        
        del self.h1
        del self.t1
        
        del self.U
        del self.K 
        del self.Ee
        del self.E
        
        del self.U1
        del self.K1
        del self.Ee1
        del self.E1

    def akc(self):
        
        dh = self.h0 - self.l - self.h
        
        if dh > 0:
            akc_el = (self.k/self.m) * dh
        
        else: 
            akc_el = 0
        
        if self.otpor_z:
            akc_ar = -(abs(self.v0)*self.v0*self.rho*self.Cd*self.A)/(2*self.m)
        
        else:
            akc_ar = 0
        a = -9.81 + akc_el + akc_ar
        
        return a

    def eng(self):
        
        dh = self.h0 - self.l - self.h
        
        if dh > 0:
            self.Ee = (1/2)*self.k*dh*dh
        
        else:
            Ee = 0
        
        self.U = self.m * 9.81 * self.h
        self.K = 0.5*self.m*(self.v0)**2
        self.E = self.U + self.K + self.Ee
        
    def _jump(self):
        
        self.a = self.akc()
        self.v0 += self.a * self.dt
        self.h += self.v0 * self.dt
        self.t += self.dt
        self.eng()

    def jump(self, t):
        
        while self.t < t:
            
            self._jump()
            self.h1.append(self.h)
            self.t1.append(self.t)
            self.Ee1.append(self.Ee)
            self.K1.append(self.K)
            self.U1.append(self.U)
            self.E1.append(self.E)
    
