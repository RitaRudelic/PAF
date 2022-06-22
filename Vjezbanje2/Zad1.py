import matplotlib.pyplot as plt


def jednoliko_gibanje(F, m, dt= 0.1):
    
    a = [F/m]
    v = [0]
    x = [0]
    t = [0]
    
    for i in range(int(10/dt)):
        
        t.append(i * dt)
        a.append(F/m)
        v.append(v[i]+a[i]*dt)
        x.append(x[i]+a[i]*dt)
    
    plt.plot(t, x)
    plt.show()


jednoliko_gibanje(10, 3)