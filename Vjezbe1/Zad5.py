import matplotlib.pyplot as plt
import numpy as np


def jednadzba(x1,y1,x2,y2, spremanje):
    k = (y2-y1)/(x2-x1)
    l = k*(-x1) + y1
    x = np.arange(x1-1, x2+1, 0.01)
    y = k * x + l
    plt.plot(x,y)

    # Draw a point at the location (3, 9) with size 1000
    plt.scatter(x1, y1, s=10, c = "red")
    plt.scatter(x2, y2, s = 10, c = "red" )
    plt.show()
    
    if spremanje == True:
        plt.savefig("Hello.pdf")

jednadzba(2, 3, 4, 5, True)   