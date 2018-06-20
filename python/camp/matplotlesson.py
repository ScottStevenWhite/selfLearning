import numpy as np
import matplotlib.pyplot as plot
import random as rnd



def cube(xList):
    newList = []
    for x in xList:
        newList.append(x * x * x)

    return newList
        
def simpleCurve():
    x_vals = np.linspace(-np.pi, np.pi, 7000, endpoint=True)
    plot.plot(cube(x_vals), np.cos(x_vals))
    plot.show()
    return

randColor = ['red', 'blue', 'purple', 'yellow', 'orange']
x_vals = []
y_vals = []
colors = []
for i in range(0, 100):
    x = rnd.randint(1, 280)
    x_vals.append(x)
    y_vals.append(rnd.randint(4,25) + x)
    colors.append(randColor[rnd.randint(0,4)])

plot.scatter(x_vals, y_vals, c=colors, alpha=.8)
plot.show()


#print(x_vals)








