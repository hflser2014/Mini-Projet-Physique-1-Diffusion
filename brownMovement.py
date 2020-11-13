# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats


class brProcess(object):
    def __init__(self, N=int(10), t=int(10), n=int(100), v=int(1), r=int(10)):
        self.N, self.t, self.n, self.v, self.r = N, t, n, v, r
        x = 0
        y = 0
        position = [[[x], [y]]]
        disArray = []
        disArrayMean = [0]
        for i in range(n - 1):
            position[0][0].append(x)
            position[0][1].append(y)

        for i1 in range(int(N * t) - 1):
            position.append([[], []])
            for i in range(n):  # 初始化
                disArray.append([])
            for i2 in range(n):
                dx = v*random.choice((-1, 1)) * random.random()
                dy = random.choice((-1, 1)) * np.sqrt(v**2 - dx**2)
                x = position[i1][0][i2] + dx
                y = position[i1][1][i2] + dy
                d = np.sqrt(x**2+y**2)
                if d > r:
                    k = d/r
                    x /= k
                    y /= k
                position[i1 + 1][0].append(x)
                position[i1 + 1][1].append(y)

                disArray[i1].append(np.sqrt(x**2 + y**2))
            disArrayMean.append(np.mean(np.array(disArray[i1])))  # 计算平均速度
        self.position = position
        self.disArrayMean = disArrayMean
        print("initialized")

    def draw(self):
        plt.figure()
        ax = np.linspace(0, self.t, len(self.disArrayMean))
        plt.plot(ax, self.disArrayMean)
        plt.show()

    def showProcess(self):
        plt.figure()
        for i in self.position:
            x = i[0]
            y = i[1]
            plt.scatter(x, y)
            plt.pause(0.01)
            plt.clf()


def gen2d(N, t, n, dimension=(50, 50)):
    plt.ion()  # matplotlib interactivate mode
    plt.gca().set_aspect('equal', adjustable='box')
    global position
    x = dimension[0] / 2
    y = dimension[1] / 2
    position = [[[x], [y]]]
    for i in range(n - 1):
        position[0][0].append(x)
        position[0][1].append(y)

    for i1 in range(int(N * t) - 1):
        position.append([[], []])
        for i2 in range(n):
            dx = random.choice((-1, 1)) * random.random()
            dy = random.choice((-1, 1)) * (1 - dx**2)**0.5
            x = position[i1][0][i2] + dx
            if x < 0:
                x = 0
            elif x > dimension[0]:
                x = dimension[0]
            y = position[i1][1][i2] + dy
            if y < 0:
                y = 0
            elif y > dimension[0]:
                y = dimension[1]
            position[i1 + 1][0].append(x)
            position[i1 + 1][1].append(y)
        x = plt.xlim(0, dimension[0])
        y = plt.ylim(0, dimension[1])
        plt.scatter(position[i1][0], position[i1][1])
        plt.show()
        plt.pause(0.001)
        plt.clf()


def gen2dC(N, t, n, v=int(5), r=int(10)):
    plt.ion()  # matplotlib interactivate mode
    plt.rcParams['figure.figsize'] = (10.0, 10.0)  # 设置figure_size尺寸

    global position
    x = 0
    y = 0
    position = [[[x], [y]]]
    for i in range(n - 1):
        position[0][0].append(x)
        position[0][1].append(y)

    for i1 in range(int(N * t) - 1):
        position.append([[], []])
        for i2 in range(n):
            dx = v*random.choice((-1, 1)) * random.random()
            dy = random.choice((-1, 1)) * np.sqrt(v**2 - dx**2)
            x = position[i1][0][i2] + dx
            y = position[i1][1][i2] + dy
            d = np.sqrt(x**2+y**2)
            if d > r:
                k = d/r
                x /= k
                y /= k
            position[i1 + 1][0].append(x)
            position[i1 + 1][1].append(y)
        x = plt.xlim(-r, r)
        y = plt.ylim(-r, r)
        plt.scatter(position[i1][0], position[i1][1])
        plt.show()
        plt.pause(0.001)
        plt.clf()

bp1 = brProcess(10, 10, 100, 5, 1000)
#bp1.showProcess()
bp1.draw()
