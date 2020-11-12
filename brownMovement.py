import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats

def brownMovement(N, t, n, starting=(0, 0)):
    #plt.ion()   # matplotlib interactivate mode

    #plt.gca().set_aspect('equal', adjustable='box')
    x = starting[0]
    y = starting[1]
    position = [[[x], [y]]]
    for i in range(n - 1):
        position[0][0].append(x)
        position[0][1].append(y)

    #plt.rcParams['figure.figsize'] = (10.0, 10.0) # 设置figure_size尺寸
    #plt.rcParams['figure.dpi'] = 500 #分辨率
    for i1 in range(int(N * t) - 1):
        position.append([[], []])
        for i2 in range(n):
            position[i1 + 1][0].append(position[i1][0][i2] + 1 -
                                       2 * random.random())
            position[i1 + 1][1].append(position[i1][1][i2] + 1 -
                                       2 * random.random())
        x = plt.xlim(-20, 20)
        y = plt.ylim(-20, 20)
        plt.scatter(position[i1][0], position[i1][1])
        plt.show()
        plt.pause(0.1)
        plt.clf()

brownMovement(1, 5, 1000)
