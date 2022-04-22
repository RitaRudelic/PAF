import matplotlib.pyplot as plt
import numpy as np
import math

class ProjectileDrop:

    def __init__(self, h0, vx):
            self.h = h0
            self.vx = vx
            self.t = [0]
            self.vy = []
            self.h_ = []
            self.x = [0]
            self.t_ = []
            self.h_.append(self.h)
            self.vy.append(self.vx)
            self.t_.append(self.t)

    def inf(self):
            print(f'Objekt je uspješno stvoren. Početna visina iznosi {self.h}, a početna brzina iznosi {self.vx}')

    def promjena_visine(self, h):
        self.h = h

    def promjena_brzine(self, v_x):
        self.vx = v_x

    def ispustanje_projektila(self, dt,):
        self.g = 9.81

        for i in range(int(10/dt)):
            
            self.t.append(i*dt)
            self.vy.append(self.vy[i]+self.g*dt)
            self.x.append(self.x[i] + self.vx*dt)
            
            if self.h <= 0:
                break
            
            self.h_.append(self.h)
            self.vy.append(self.vy)
            self.t_.append(self.t)

        return self.h, self.vy, self.t, self.x

    def vrijeme_padanja(self, dt):
        self.ispustanje_projektila(dt)
        t = self.t_[-1]
        
        return(t)



    


