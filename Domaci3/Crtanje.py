from codecs import xmlcharrefreplace_errors
from matplotlib import lines
import matplotlib.pyplot as plt
import os

print(os.listdir())

c = 0
x = []
v = []
a = []
t = []
linije = [[],[],[],[]]
f1 = open("e.txt","r")
lines = f1.readlines()
for line in lines: 
    linije[c] = line.split(" ") 

f1.close()    
x = linije[0] 
v = linije[1]
a = linije[2]
t = linije[3]

x = x[:-1]  
v = v[:-1]  
a = a[:-1]
t = t[:-1]

X = [float(a) for a in x] 
V = [float(a) for a in v] 
A = [float(a) for a in a]
T = [float(a) for a in t]

print(T)
plt.plot(X, T, c="r", label ="xt - graf")
plt.show()

plt.plot(V , T, c="b", label ="vt - graf")
plt.show()

plt.plot(A , T, c="g", label ="at - graf")
plt.show()
