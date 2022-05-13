import math as ma
import matplotlib.pyplot as plt

class Projectile:
    
    def __init__(self, v0 , x0, y0, theta, m, A, Cd):   
        
        self.x = x0
        self.y = y0
        self.v0 = v0
        self.theta = theta
        self.vx = v0*ma.cos(self.theta)
        self.vy = v0*ma.sin(self.theta)
        self.y0 = y0
        self.x0 = x0
        theta = (theta/180)* ma.pi
        self.masa = m
        self.povrsina = A
        self.Cd = Cd
        
        self.otpor_y = y0
        self.rho = 1.125
        self.dt = 0.01
        self.list_x = [x0]
        self.list_y = [y0]

    def reset(self):
        
        del self.x
        del self.y
        del self.v0
        del self.vx
        del self.vy
        del self.y0
        del self.x0
        del self.theta 
        del self.masa   
        del self.povrsina
        del self.Cd    
        
        del self.otpor_y
        del self.rho
        del self.dt
        del self.list_x
        del self.list_y

    def back(self):
        
        del self.otpor_y
        del self.vx
        del self.vy
        del self.x
        del self.y
        
        self.list_x.clear()
        self.list_y.clear()
        self.x = self.x0
        self.y = self.y0
        self.otpor_y = self.y0
        self.list_x.append(self.x)
        self.list_y.append(self.y)
        self.vx = self.v0*ma.cos(self.theta)
        self.vy = self.v0*ma.sin(self.theta)   


    def otpor_z_x(self, x):
        
        if self.theta < ma.pi/2:            
            Fx = -((self.vx + x)**2 * self.povrsina * self.Cd* self.rho ) / 2
        
        else:                                               
            Fx = ((self.vx + x)**2 * self.povrsina * self.Cd* self.rho ) / 2
        
        return Fx

    def otpor_z_y(self, x):
        
        if self.otpor_y > self.y:         
            Fy = ((self.vy + x)**2 * self.povrsina * self.Cd * self.rho ) / 2   
        
        else:
            Fy = -((self.vy + x)**2 * self.povrsina * self.Cd * self.rho ) / 2
        
        return Fy

    def gibanje(self):
        
        while True:
            
            if self.y >= 0:
                
                Akceleracija = self.otpor_z_x(0) / self.masa
                self.vx = self.vx + Akceleracija*self.dt
                self.x = self.x + self.vx * self.dt
                self.list_x.append(self.x)

                Akceleracija_y = self.otpor_z_y(0) / self.masa
                self.vy = self.vy - 9.81*self.dt + Akceleracija_y*self.dt
                self.otpor_y = self.y
                self.y = self.y + self.vy * self.dt
                self.list_y.append(self.y)
            
            else:
                break

            
    def Runge_Kutta(self):
        
        while True:
            
            if self.y >=0:
                
                k1vx = self.otpor_z_x(0) / self.masa * self.dt
                k1x = self.vx * self.dt
                
                k2vx = self.otpor_z_x(0.5*k1vx) / self.masa * self.dt
                k2x = (self.vx + 0.5 * k1vx) * self.dt
                
                k3vx = self.otpor_z_x(0.5*k2vx) / self.masa * self.dt
                k3x = (self.vx + 0.5 * k2vx) * self.dt
                
                k4vx = self.otpor_z_x(0.5*k3vx) / self.masa * self.dt
                k4x = (self.vx + k3vx) * self.dt
                
                self.vx = self.vx + (1/6)*(k1vx + 2 * k2vx + 2 * k3vx + k4vx)
                self.x = self.x + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
                
                self.list_x.append(self.x)
                    
                k1vy = ((self.otpor_z_y(0) / self.masa)-9.81) * self.dt
                k1y = self.vy * self.dt
                
                k2vy = ((self.otpor_z_y(0.5*k1vy) / self.masa)-9.81) * self.dt
                k2y = (self.vy + 0.5 * k1vy) * self.dt
                
                k3vy = ((self.otpor_z_y(0.5*k2vy) / self.masa)-9.81) * self.dt
                k3y = (self.vy + 0.5 * k2vy) * self.dt

                k4vy = ((self.otpor_z_y(0.5*k3vy) / self.masa)-9.81) * self.dt
                k4y = (self.vy + k3vy) * self.dt
                
                self.vy = self.vy + (1/6)*(k1vy + 2 * k2vy + 2 * k3vy + k4vy)
                self.y = self.y + (1/6)*(k1y + 2 * k2y + 2 * k3y + k4y)
                
                self.list_y.append(self.y)
            
            else:
                break

    def plot(self):
        
        plt.plot(self.list_x,self.list_y)
        plt.show()

    def domet_koef(self):
        
        self.Cd= 0
        d = []
        k = []
        
        for i in range(1000):
            
            x0 = self.x
            self.Runge_Kutta()
            domet = abs(self.list_x[-1] - x0)
            self.back()
            d.append(domet)
            k.append(self.Cd)
            self.Cd += 0.1
        
        return d, k

    def domet_m(self):
        
        self.masa= 0.1
        d1 = []
        m = []
        
        for i in range(1000):
            
            x0 = self.x
            self.Runge_Kutta()
            domet = abs(self.list_x[-1] - x0)
            self.back()
            d1.append(domet)
            m.append(self.masa)
            self.masa += 0.1
        
        return d1, m


    def plot_domet(self):
        
        d,k = self.domet_koef()
        
        plt.plot(d,k)
        plt.show()

        d1,m = self.domet_m()
        
        plt.plot(d1,m)
        plt.show()