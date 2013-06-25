# implement the example graphs/integral from pyx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')

def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1, a2, b1, b2):
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)
    return (num / denom)*db + b1

def c1(x):
    return 2*x + 1

def c2(x):
    return -x + 5

def get_basic_plot(xlow, xhigh, ylow, yhigh, dx, xbound):
    x = np.arange(xlow, xhigh, dx)
    y1 = c1(x)
    y2 = c2(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y1, color='b')
    ax.plot(x, y2, color='r')
    ax.vlines(xbound, ylow, yhigh, color='g')
    ax.axis([xlow, xhigh, ylow, yhigh])
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    return ax, fig, x, y1, y2

def feasible_plt(fname, save=True, show=False, **kwargs):
    xlow, xhigh, ylow, yhigh = 0, 5, 0, 5
    dx = 0.01
    xbound = 4
    ax, fig, x, y1, y2 = get_basic_plot(xlow, xhigh, ylow, yhigh, dx, xbound)
    
    i1 = seg_intersect(np.array([xlow, ylow]), \
                           np.array([xlow, yhigh]), \
                           np.array([x[0], y1[0]]), \
                           np.array([x[-1], y1[-1]]))
    
    i2 = seg_intersect(np.array([x[0], y1[0]]), \
                           np.array([x[-1], y1[-1]]), \
                           np.array([x[0], y2[0]]), \
                           np.array([x[-1], y2[-1]]))
    
    i3 = seg_intersect(np.array([xbound, ylow]), \
                           np.array([xbound, yhigh]), \
                           np.array([x[0], y2[0]]), \
                           np.array([x[-1], y2[-1]]))
    
    verts = ( (0,0), (i1[0],i1[1]), (i2[0],i2[1]), (i3[0],i3[1]), (xbound,0) )
    patch = pch.Polygon(verts, closed=True, facecolor='y', alpha=0.5)
#    print verts
    ax.add_patch(patch)
    if 'title' in kwargs:
        ax.set_title(kwargs.get('title'))
    if show:
        plt.show()
    if save:
        plt.savefig(fname)

def infeasible_plt(fname):
    xlow, xhigh, ylow, yhigh = 0, 5, 0, 5
    dx = 0.01
    xbound = 4
    ax, fig, x, y1, y2 = get_basic_plot(xlow, xhigh, ylow, yhigh, dx, xbound)
    
    ybound = 4
    ax.axhline(y=ybound, xmin=xlow, xmax=xhigh, color='y')

    i1 = seg_intersect(np.array([xlow, ybound]), \
                           np.array([xhigh, ybound]), \
                           np.array([x[0], y1[0]]), \
                           np.array([x[-1], y1[-1]]))
    
    i2 = seg_intersect(np.array([x[0], y1[0]]), \
                           np.array([x[-1], y1[-1]]), \
                           np.array([x[0], y2[0]]), \
                           np.array([x[-1], y2[-1]]))

    i3 = seg_intersect(np.array([xlow, ybound]), \
                           np.array([xhigh, ybound]), \
                           np.array([x[0], y2[0]]), \
                           np.array([x[-1], y2[-1]]))
    
    verts = ((i1[0],i1[1]), (i2[0],i2[1]), (i3[0],i3[1]))
    patch = pch.Polygon(verts, closed=True, facecolor='r', alpha=0.5)
    
    ax.add_patch(patch)
    if 'title' in kwargs:
        ax.set_title(kwargs.get('title'))
    if show:
        plt.show()
    if save:
        plt.savefig(fname)

if __name__=="__main__":
    feasible_plt("feasible.png", title=r'A Feasible Solution Space')
    infeasible_plt("infeasible.png", title=r'A Infeasible Linear Program')
    feasible_plt("geometric.png", title=r'LP Geometric View')
    
