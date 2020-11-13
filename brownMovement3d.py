import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats
from mayavi import mlab

def matDraw(position, i1):
    ax = plt.subplot(121, projection='3d')
    ax.set_xlim3d([-50, 50])
    ax.set_ylim3d([-50, 50])
    ax.set_zlim3d([-50, 50])
    ax.scatter(position[i1][0], position[i1][1], position[i1][2])

    plt.show()
    plt.pause(0.0001)
    plt.clf()


def mayaviDraw(position,dimension):
    a0=range(0,dimension[2],5)
    a = a0
    for i in range(len(a)-1):
        a = a+a0
    x = position[-1][0]
    x.extend(a)
    y = position[-1][1]
    y.extend(a)
    z = position[-1][2]
    z.extend(a)

    coor = [x, y, z]

    coor = np.stack(coor, axis=0)
    kde = stats.gaussian_kde(coor)
    density = kde(coor)

    mlab.figure('DensityPlot')
    mlab.points3d(x, y, z, density, scale_mode='none', scale_factor=0.07)
    mlab.axes()
    mlab.show()
    mlab.clf()


def gen3d(N, t, n, dimension=(50, 50, 50)):
    x, y, z = dimension[0]/2, dimension[1]/2, dimension[2]/2
    position = [[[x], [y], [z]]]
    disArray = []
    disArrayMean = []

    for i in range(n - 1):  #生成初始点矩阵
        position[0][0].append(x)
        position[0][1].append(y)
        position[0][2].append(z)

    for i1 in range(int(N * t) - 1):  #随机行走，每个循环生成一帧中的情况
        position.append([[], [], []])
        for i in range(n):  #初始化
            disArray.append([])
        for i2 in range(n):  #每个循环计算出一个点在一帧中的变化
            position[i1 + 1][0].append(position[i1][0][i2] + 1 -
                                       2 * random.random())
            position[i1 + 1][1].append(position[i1][1][i2] + 1 -
                                       2 * random.random())
            position[i1 + 1][2].append(position[i1][2][i2] + 1 -
                                       2 * random.random())
            #'''
            x = position[i1][0][i2]
            y = position[i1][1][i2]
            z = position[i1][2][i2]

            disArray[i1].append((x**2 + y**2 + z**2)**0.5)
            disArrayMean.append(np.mean(np.array(disArray[i1])))  #计算平均速度
    return position,disArrayMean,N

def drawDP(input):
    disArray=input[1]
    N = input[2]
    #plt.ion()
    fig = plt.figure()
    vt = fig.add_subplot(111)
    for i in range(len(disArray)):
        vt.plot(np.linspace(0, (i + 1) / N, i + 1), disArray[0:i+1])
        plt.show()
        plt.pause(1)
        plt.clf()
    '''
    plt.ion()  # matplotlib interactivate mode
    fig = plt.figure()

            ax = plt.subplot(121, projection='3d')

        ax.set_xlim3d([-50, 50])
        ax.set_ylim3d([-50, 50])
        ax.set_zlim3d([-50, 50])
        ax.scatter(position[i1][0], position[i1][1], position[i1][2])

        plt.show()
        plt.pause(1)
        plt.clf()
        #matDraw(position,i1)
        #mayaviDraw(position,dimension)
    plt.show()
'''
drawDP(gen3d(10, 1, 10))
