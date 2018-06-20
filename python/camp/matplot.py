import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def simpleCurve():
    x_vals = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    plt.plot(x_vals, np.cos(x_vals))
    plt.show()
    return

def randomScatter():
    x_vals = []
    y_vals = []
    colors = []
    for i in range(0, 100):
        x = rnd.randint(1, 25)
        x_vals.append(x)
        y_vals.append(x*x + rnd.randint(1, 200))
        if x_vals[i] > y_vals[i]:
            colors.append('red')
        else:
            colors.append('blue')
    plt.scatter(x_vals, y_vals, c=colors, alpha=1)
    plt.show()
    return

def listAvg(d):
    return sum(d)/len(d)

def randomBar(d1, d2, d3):
    x_vals = np.arange(3)
    data = [listAvg(d1), listAvg(d2), listAvg(d3)]
    b1, b2, b3 = plt.bar(x_vals, data)
    b1.set_facecolor('red')
    b2.set_facecolor('blue')
    b3.set_facecolor('green')
    plt.xticks(x_vals, ('1st', '2nd', '3rd'))
    plt.show()
    return

#simpleCurve()
randomScatter()
#dd1 = [1, 2, 3, 4, 5]
#dd2 = [55, 6, 12, 8]
#dd3 = [11, 12]
#randomBar(dd1, dd2, dd3)
