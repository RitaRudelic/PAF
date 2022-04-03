
import matplotlib.pyplot as plt
import math
import numpy as np


class particle:
   
    def __init__(self):
        self.g = -9.81
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
       
    def set_initial_conditions(self, v0, theta, x0, y0, dt):
        self.vx += [v0*np.cos(np.radians(theta))]
        self.vy += [v0*np.sin(np.radians(theta))]
        self.theta = theta
        self.x +=[x0]
        self.y += [y0]
        self.v0=v0
        self.dt=dt
   
    def reset(self):
        self.vx = []
        self.vy = []
        
        self.x = []
        self.y = []

    def __move(self):
        self.vx += [self.vx[len(self.vx)-1]]
        self.vy += [self.vy[len(self.vy)-1]+self.g*self.dt]
       
        self.x += [self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
        self.y += [self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]

    def range(self):
        while(self.y[-1]>=0):
            self.__move()
        return(self.x[-1])

   
    def plot_trajectory(self):
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x,self.y)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*np.radians(self.theta)))/9.81
        return D


    def total_time(self):
        t = 0
        while self.y[-1] >= 0 and len(self.y) == 1 and len(self.y) == 0:
            self.__move()
            t = t + self.dt
        return t
        
    def max_speed(self):
        while self.y[-1] >= 0 and len(self.y) == 1 and len(self.y) == 0:
            self.__move()
        return max(self.vy)


    def velocity_to_hit_target(self, mx, my, r):
        self.mx = mx
        self.my = my
        self.r = r
        d_list = []
        v_list = []
        pogodena = False
    
        # dio koji racunau brzinu
        for self.v0 in range(100):
            self.vx += [self.vx[len(self.vx)-1]]
            self.vy += [self.vy[len(self.vy)-1]+self.g*self.dt]
            self.__move()
            D =  math.sqrt((self.mx-self.x)**2 + (self.my-self.y)**2) 
            if D <= self.r:
                pogodena = True
                break
            else: 
                d_list.append(D - self.r)
                v_list.append(self.v0)
        
        if pogodena:
            
            print("Brzina potrebna za pogoditi metu iznosi: {:.2f}m/s".format(self.v0))

            # dio koji crta metu
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.set_initial_conditions(self.v0, self.theta, self.x, self.y, self.dt )
            self.plot_trajectory()
            self.reset()

        else:
           
            d = min(d_list)
            print("Nemoguce je pogoditi metu sa zadanim kutem.")
            print("Najmanja udaljenost od mete za zadani kut iznosi: {:.2f}".format(d))

            indeks = d_list.index(d)
            v = v_list[indeks]

            # dio koji crta metu
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.set_initial_conditions(v, self.theta, self.x, self.y, self.dt )
            self.plot_trajectory()
            self.reset()

    def angle_to_hit_target(self, mx, my, r):
        self.mx = mx
        self.my = my
        self.r = r
        
        d_lista = []
        th_lista = []
        pogodena = False

        # dio koji racuna kut
        for self.theta in range(100):
            self.kut = self.theta*math.pi/180
            self.vx = self.v0*math.cos(self.kut)
            self.vy = self.v0*math.sin(self.kut)
            self.__move()
            D =  math.sqrt((self.mx-self.x)**2 + (self.my-self.y)**2) 
            if D <= self.r:
                pogodena = True
                break
            else:
                d_lista.append(D - self.r)
                th_lista.append(self.theta)

        if pogodena:
            
            print("Kut koji je potreban za pogoditi metu je: {}°".format(self.theta))
            
            # dio koji crta metu
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.set_initial_conditions(self.v0, self.theta, self.x, self.y, self.dt)
            self.plot_trajectory()
            self.reset()      

        else: 
            
            d = min(d_lista)
            print("Nemoguce je pogoditi metu sa zadanom brzinom.")
            print("Najmanja udaljenost od mete za zadanu brzinu je: {:.2f}m.".format(d))
            
            indeks = d_lista.index(d)
            theta = th_lista[indeks]

            # dio koji crta metu
            x = []
            y = [] 
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.set_initial_conditions(self.v0, theta, self.x, self.y, self.dt )
            self.plot_trajectory()
            self.reset()


