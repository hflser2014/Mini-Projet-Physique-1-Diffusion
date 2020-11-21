import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker


def func(x, a, k):
    return k*x**a


def output(xArray, yArray):
    #    ax = plt.gca()
    # plt.style.use('seaborn')

    popt, pcov = curve_fit(func, xArray, yArray, maxfev=500000)
    a = popt[0]
    k = popt[1]
    print(a, k)
    x = np.linspace(xArray[0], xArray[-1], 1000)
    y = func(x, a, k)
    '''
    for (a,b) in zip(xArray,yArray):
        plt.plot([0,a],[b,b],linewidth=1,linestyle='--',color='gray')
        plt.plot([a,a],[0,b],linewidth=1,linestyle='--',color='gray')
    '''
    '''
    tick_spacing = 0.01
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # plt.text(0.025,0.05,"y = %fx+%f"%(k,b))
    '''
    plot1 = plt.scatter(xArray, yArray, marker='o')
    plot2 = plt.plot(x, y)
    plt.grid()
    plt.show()
