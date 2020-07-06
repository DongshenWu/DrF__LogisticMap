from matplotlib import pyplot as plt
import numpy as np

def logistic_map (r, x):
    xnew = r * (x - x ** 2)
    return xnew

xini = np.linspace(0, 1, 100)
yini = []

def plot_graph(r,w):
    for i in xini:
        yini.append(logistic_map(r, i))
    plt.plot(xini, yini, color = 'blue')
    plt.plot(xini, xini, color = 'red')
    del yini[:]
    xvals = []
    yvals = []
    x = 0.1
    for i in range(2000):
        fx = logistic_map(r, x)
        xvals.extend([x, x])
        yvals.extend([x, fx])
        x = fx
    plt.plot(xvals, yvals, color = 'black', linewidth = w)
    plt.title('Cobweb Diagram: r = {}'.format(r))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()


plt.figure(figsize = (10, 8))
plt.subplot(2,2,1)
plot_graph(2.5,1)
plt.subplot(2,2,2)
plot_graph(3.35,1)
plt.subplot(2,2,3)
plot_graph(3.5,1)
plt.subplot(2,2,4)
plot_graph(4,.1)
plt.subplots_adjust(wspace = .35, hspace = .4)
plt.show()