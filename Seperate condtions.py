from matplotlib import pyplot as plt
import numpy as np

def logistic_map (r, x):
    xnew = r * (x - x ** 2)
    return xnew

xini = np.linspace(.01, .99, 99)

def plot_graph (r, ax):
    for xold in xini:
        plt.plot(0, xold, ',')
        for i in range(1, 51):
            xnew = logistic_map(r, xold)
            xold = xnew
            plt.plot(i, xnew, ',')

    plt.xlabel('iteration')
    plt.ylabel('x values')
    plt.title('r = {}'.format(r))
    ax.set_clip_on(False)
    ax.set_xticks(range(0, 51, 10))
    ax.set_yticks([i / 10 for i in range(0, 11)])

def driver ():
    plt.figure(figsize = (10, 8))
    ax1 = plt.subplot(2, 3, 1)
    plot_graph(1.5, ax1)
    ax2 = plt.subplot(2, 3, 2)
    plot_graph(2.5, ax2)
    ax3 = plt.subplot(2, 3, 3)
    plot_graph(3.3, ax3)
    ax4 = plt.subplot(2, 3, 4)
    plot_graph(3.5, ax4)
    ax5 = plt.subplot(2, 3, 5)
    plot_graph(4.0, ax5)
    plt.subplots_adjust(hspace = .4, wspace = .35)
    plt.show()

driver()
