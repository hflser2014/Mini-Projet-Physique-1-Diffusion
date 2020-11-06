import matplotlib.pyplot as plt
import numpy as np
import random

def randomwalk(N,t,starting = (0,0)):
    x = starting[0]
    y = starting[1]
    xsum = [x]
    ysum = [y]
    #plt.rcParams['figure.figsize'] = (10.0, 10.0) # 设置figure_size尺寸
    #plt.rcParams['figure.dpi'] = 500 #分辨率
    for i in range(int(N*t)):
        y += 1-2*random.random()
        x += 1-2*random.random()
        xsum.append(x)
        ysum.append(y)
    plt.grid()
    plt.plot(starting[0],starting[1],"ro")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(xsum,ysum)
    plt.plot(x,y,"ro")
    plt.show()
    
def randomwalk3d(N,t,starting = (0,0,0)):
    plt.figure()
    plt.axes(projection='3d')
    x,y,z = starting[0],starting[1],starting[2]
    xsum,ysum,zsum=[x],[y],[z]
    for i in range(int(N*t)):
        x += 1-2*random.random()
        y += 1-2*random.random()
        z += 1-2*random.random()
        xsum.append(x)
        ysum.append(y)
        zsum.append(z)
    plt.grid()
    plt.plot(starting[0],starting[1],starting[2],"ro")
    plt.gca().set_aspect('auto', adjustable='box')
    plt.plot(xsum,ysum,zsum)
    plt.plot(x,y,z,"ro")
    plt.show()
        
randomwalk3d(2000,10)

