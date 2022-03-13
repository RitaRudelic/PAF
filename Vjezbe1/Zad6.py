import matplotlib.pyplot as plt
import numpy as np

def crtez_kruznice_i_tocke(x_1,y_1,x_2,y_2,r,spremanje):

    figure, axes = plt.subplots()
    draw_circle = plt.Circle((x_2, y_2), r,fill=False)

    axes.set_aspect(1)
    axes.add_patch(draw_circle)
    plt.title('Circle')
    plt.scatter(x_1,y_1)
    plt.show()

    a = np.array([x_1,y_1])
    b = np.array([x_2,y_2])
    d = np.linalg.norm(a-b)

    if d > r:
        print("Točka je izvan kružnice.")
    elif d < r:
        print("Točka je unutar kružnice.")
    else:
        print("Točka je na kružnici.")

    if spremanje == True:
        plt.savefig("foo.png")    


crtez_kruznice_i_tocke(1,0,2,0,1,True)