import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

def brownMovement(N,t,n,starting = (0,0)):
    plt.ion()   # matplotlib interactivate mode

    #plt.gca().set_aspect('equal', adjustable='box')
    x = starting[0]
    y = starting[1]
    position = [[[x]
                ,[y]]]
    for i in range(n-1):
        position[0][0].append(x)
        position[0][1].append(y)

    #plt.rcParams['figure.figsize'] = (10.0, 10.0) # 设置figure_size尺寸
    #plt.rcParams['figure.dpi'] = 500 #分辨率
    for i1 in range(int(N*t)-1):
        position.append([[],[]])
        for i2 in range(n):
            position[i1+1][0].append(position[i1][0][i2]+1-2*random.random())
            position[i1+1][1].append(position[i1][1][i2]+1-2*random.random())
        x = plt.xlim(-20,20)
        y = plt.ylim(-20,20)            
        plt.scatter(position[i1][0],position[i1][1])
        plt.show()
        plt.pause(0.1)
        plt.clf()

        #plt.scatter(position,position)
    plt.show()

def brownMovement3d(N,t,n,starting = (0,0,0)):
    plt.ion()   # matplotlib interactivate mode
    x,y,z = starting[0],starting[1],starting[2]
    position = [[[x],[y],[z]]]
    for i in range(n-1):
        position[0][0].append(x)
        position[0][1].append(y)
        position[0][2].append(z)
    for i1 in range(int(N*t)-1):
        position.append([[],[],[]])
        for i2 in range(n):
            position[i1+1][0].append(position[i1][0][i2]+1-2*random.random())
            position[i1+1][1].append(position[i1][1][i2]+1-2*random.random())
            position[i1+1][2].append(position[i1][2][i2]+1-2*random.random())


        ax = plt.subplot(111, projection='3d')

        ax.set_xlim3d([-50, 50])
        ax.set_ylim3d([-50, 50])
        ax.set_zlim3d([-50, 50])

        ax.scatter(position[i1][0],position[i1][1],position[i1][2])#,c="green")
        plt.show()
        plt.pause(0.01)
        plt.clf()

        #plt.scatter(position,position)
    plt.show()

brownMovement3d(1,1000,1000)

