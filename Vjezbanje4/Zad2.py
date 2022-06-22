import calculus as cal
import matplotlib.pyplot as plt

def f1(x):
    return(x**2)

a,b = cal.integ(f1, 0, 1, 100)
print(a,b)

plt.figure(figsize=(13, 5))

for i in range(50, 1000, 50): 
    plt.scatter(i, cal.integ(f1, a, b, i)[0], c = 'darkslategray')
    plt.scatter(i, cal.integ(f1, a, b, i)[1], c = 'cadetblue')
    plt.scatter(i, cal.integ1(f1, a, b, i), c = 'teal')

plt.show()