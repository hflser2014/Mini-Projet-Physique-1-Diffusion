import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
x=plt.xlim(0,20)
y=plt.ylim(0,20)
pointsum=(msum,psum)
plt.plot(msum,psum,"ro")

def brownMovement3d(N,t,n,starting = (0,0,0)):#n=粒子数
    a,b,c = starting[0],starting[1],starting[2]
    position = [[[a],[b],[c]]]
    msum=[0]
    psum=[0]
    for i in range(n-1):
        position[0][0].append(a)
        position[0][1].append(b)
        position[0][2].append(c)
    for i1 in range(int(N*t)-1):
        position.append([[],[],[]])
        m=0
        for i2 in range(n):
            position[i1+1][0].append(position[i1][0][i2]+1-2*random.random())
            position[i1+1][1].append(position[i1][1][i2]+1-2*random.random())
            position[i1+1][2].append(position[i1][2][i2]+1-2*random.random())
            p1=np.array(([position[i1][0]],[position[i1][1]][position[i1][2]]))
            p2=np.array(([position[i1+1][0]],[position[i1+1][1]][position[i1+1][2]]))
            dis=np.sqrt((np.sum((p1-p2)**2))
            psum.append(dis)
            msum.append(m)
            
            plt.plot(msum,psum,"ro")
            plt.plot(msum,psum)
            m+=1
        #plt.scatter(position,position)
    plt.show()

brownMovement3d(1,1000,1000)