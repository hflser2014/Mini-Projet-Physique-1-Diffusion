# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random
import adjLine
from scipy import stats
from scipy import constants
from mayavi import mlab


class brProcess(object):
    def __init__(self, N=int(10), t=int(10000), n=int(100), v=int(5), r=int(10)):
        '''Initialize the object

        and generate a list containing all the process concerning the diffusion.'''
        self.N, self.t, self.n, self.v, self.r = N, t, n, v, r
        x = 0
        y = 0
        position = [[[x], [y]]]
        disArray = []
        disArrayMean = [0.01]
        for i in range(n - 1):
            position[0][0].append(x)
            position[0][1].append(y)

        for i1 in range(int(N * t) - 1):
            position.append([[], []])
            disArray.append([])
            for i2 in range(n):
                dx = v/N*random.choice((-1, 1)) * random.random()
                dy = random.choice((-1, 1)) * np.sqrt((v/N)**2 - dx**2)
                x = position[i1][0][i2] + dx
                y = position[i1][1][i2] + dy
                d = np.sqrt(x**2+y**2)
                if d > r:
                    k = (2*r-d)/r
                    x *= k
                    y *= k
                position[i1 + 1][0].append(x)
                position[i1 + 1][1].append(y)

                disArray[i1].append(np.sqrt(x**2 + y**2))
            disArrayMean.append(np.mean(np.array(disArray[i1])))  # 计算平均速度
        self.position = position
        self.disArrayMean = disArrayMean
        print("initialized")

    def drawfit(self):
        '''Draw the graph of the average displacement change with time 

        Draw the graph of the average displacement change with time'''
        ax = np.linspace(0, self.t, len(self.disArrayMean))
        plt.xlabel("time/s")
        plt.ylabel("mean of displacement")
        adjLine.output(ax, self.disArrayMean)

    def showProcess(self):
        plt.ion()
        for i in self.position:
            x = i[0]
            y = i[1]
            plt.xlim(-self.r, self.r)
            plt.ylim(-self.r, self.r)
            plt.scatter(x, y)
            plt.show()
            plt.pause(0.01)
            plt.clf()

    def calcDen(self):
        coor = self.position[-1]

        coor = np.stack(coor, axis=0)
        x = coor[0]
        y = coor[1]

        # Define the borders
        deltaX = (max(x) - min(x))/10
        deltaY = (max(y) - min(y))/10
        self.xmin = min(x) - deltaX
        self.xmax = max(x) + deltaX
        self.ymin = min(y) - deltaY
        self.ymax = max(y) + deltaY
        print(self.xmin, self.xmax, self.ymin, self.ymax)
        # Create meshgrid
        self.xx, self.yy = np.mgrid[self.xmin:self.xmax:100j,
                                    self.ymin:self.ymax:100j]

        positions = np.vstack([self.xx.ravel(), self.yy.ravel()])
        values = np.vstack([x, y])
        kernel = stats.gaussian_kde(values)
        self.density_distribute = np.reshape(
            kernel(positions).T, self.xx.shape)

    def analyseDen(self):
        self.density_distribute = []
        self.listEntropy = []
        for i in range(len(self.position)-1):
            Entropy = 0
            coor = self.position[i+1]

            coor = np.stack(coor, axis=0)
            x = coor[0]
            y = coor[1]

            # Define the borders
            deltaX = deltaY = 2*self.r/10
            self.xmin = -self.r - deltaX
            self.xmax = self.r + deltaX
            self.ymin = -self.r - deltaY
            self.ymax = self.r + deltaY
            # Create meshgrid
            self.xx, self.yy = np.mgrid[self.xmin:self.xmax:100j,
                                        self.ymin:self.ymax:100j]
            # positions of which we calculate density
            positions = np.vstack([self.xx.ravel(), self.yy.ravel()])

            # Initialize kernel
            values = np.vstack([x, y])
            kernel = stats.gaussian_kde(values)
            self.density_distribute = np.reshape(
                kernel(positions).T, self.xx.shape)
            frame = self.density_distribute

            for i1 in frame:
                for i2 in i1:
                    Entropy -= constants.k*i2*np.log(i2)
            self.listEntropy.append(Entropy)
        print("analysed")

    def draw(self):
        self.analyseDen()

        fig = plt.figure(figsize=(13, 7))

        ax = plt.subplot(221)
        ax.set_xlim(self.xmin, self.xmax)
        ax.set_ylim(self.ymin, self.ymax)
        cfset = ax.contourf(
            self.xx, self.yy, self.density_distribute, cmap='coolwarm')
        ax.imshow(np.rot90(self.density_distribute), cmap='coolwarm',
                  extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        cset = ax.contour(self.xx, self.yy,
                          self.density_distribute, colors='k')
        ax.clabel(cset, inline=1, fontsize=10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.title('2D Gaussian Kernel density estimation')

        ax = plt.subplot(222, projection='3d')
        surf = ax.plot_surface(self.xx, self.yy, self.density_distribute,
                               rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
        ax.set_xlim3d(-self.r, self.r)
        ax.set_ylim3d(-self.r, self.r)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('PDF')
        ax.set_title('Surface plot of Gaussian 2D KDE')
        # add color bar indicating the PDF
        fig.colorbar(surf, shrink=0.5, aspect=5)
        ax.view_init(60, 35)

        ax = plt.subplot(223)
        ax.set_xlim(-self.r, self.r)
        ax.set_ylim(-self.r, self.r)
        ax.scatter(self.position[-1][0], self.position[-1][1])

        ax = plt.subplot(224)
        ax.set_xlabel("time")
        ax.set_ylabel("entropy")
        plt.plot(np.linspace(0, self.t, len(
            self.listEntropy)), self.listEntropy)
        plt.show()


bp1 = brProcess(10, 100, 1000, 5, 10)
# bp1.showProcess()
bp1.draw()
