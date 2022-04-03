def der(f, x, dx, m):
    
    if m==2:
        return(f(x+dx)-f(x))/dx
    else:
        return((f(x+dx)-f(x-dx))/2*dx)

def der1(f, a, b, dx, m=3):
    x = []
    dfx = []

    for i in range(int((b-a)/dx)):
        x.append(a+i*dx)
        dfx.append(der(f, a+i*dx, dx, m))
    
    return(x, dfx)

def integ(f, a, b, N):
    dx = (b-a)/float(N)
    sumaupper=0.
    sumalower=0.
    for i in range(N):
        sumalower += f(a + i*dx)*dx
        sumaupper += f(a + (i+1)*dx)*dx

    return sumalower, sumaupper   

def integ1(f, a, b, N):
    dx = (b-a)/float(N)
    x = (f(a)+f(b))/2

    for i in range(1, N):
        x += f(a+i*dx)
    
    return x*dx 

