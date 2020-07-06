import matplotlib.pyplot as plt
import numpy as np

def logistic_map (r, x):
    return r * (x - x ** 2)

growth = np.linspace(.0001, 4, 40000)
xvals, yvals = [], []
plt.figure(figsize = (10, 8))

for r in growth:
    xold = 0.5
    for i in range(1, 900):
        xnew = logistic_map(r, xold)
        xold = xnew
    xss = xnew
    for i in range(1, 100):
        xnew = logistic_map(r, xold)
        xold = xnew
        yvals.append(xnew)
        xvals.append(r)
        if abs(xnew - xss) < .001:
            break
    plt.plot(xvals, yvals, 'k,', alpha = .25)
    del xvals[:]
    del yvals[:]
plt.title('Logistic map')
plt.xlabel('growth rate r')
plt.ylabel('x values')
plt.show()
