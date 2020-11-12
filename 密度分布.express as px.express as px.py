'''import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
 
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import MinMaxScaler
 
 
def dummy_data(size, center_size):
    # 制造一批数据。
    x, y = make_blobs(n_samples=size, centers=center_size, n_features=2, random_state=1)
 
    scaler = MinMaxScaler()
    # MinMaxScaler：归一到 [ 0，1 ]
    scaler.fit(x)
    x = scaler.transform(x)
 
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.grid()
    plt.show()
 
    return x, y'''
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('seaborn-white')

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
    fig = plt.figure() 


    x,y,z = starting[0],starting[1],starting[2]
    position = [[[x],[y],[z]]]
    disArray = []
    disArrayMean = []

    for i in range(n-1):
        position[0][0].append(x)
        position[0][1].append(y)
        position[0][2].append(z)
    for i1 in range(int(N*t)-1):
        position.append([[],[],[]])
        for i in range(n):
            disArray.append([])
        for i2 in range(n):
            position[i1+1][0].append(position[i1][0][i2]+1-2*random.random())
            position[i1+1][1].append(position[i1][1][i2]+1-2*random.random())
            position[i1+1][2].append(position[i1][2][i2]+1-2*random.random())

            x = position[i1][0][i2]
            y = position[i1][1][i2]
            z = position[i1][2][i2]

            disArray[i2].append((x**2+y**2+z**2)**0.5)

        ax = plt.subplot(131, projection='3d')


        ax.set_xlim3d([-50, 50])
        ax.set_ylim3d([-50, 50])
        ax.set_zlim3d([-50, 50])

        ax.scatter(position[i1][0],position[i1][1],position[i1][2])#,c="green")

        disArrayMean.append(np.mean(np.array(disArray[i1]))) #绘制速度
        vt= fig.add_subplot(132)
        vt.plot(np.linspace(0,(i1+1)/N,i1+1),disArrayMean)
        def f(x, y,z):
            md=plt.subplot(133, projection='3d') 
            md.set_xlim3d([-50, 50])
            md.set_ylim3d([-50, 50])
            md.set_zlim3d([-50, 50])

            X, Y, Z = np.meshgrid(x, y, z)
            H = f(X, Y, Z)

            # 生成等高线图
            plt.contour(X, Y ,Z, colors='black')
            return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
        f(x, y, z)
        plt.show()
        plt.pause(0.0001)
        plt.clf()
            
        #plt.scatter(position,position)
    plt.show()

brownMovement3d(1,1000,10)





 
 
'''if __name__ == '__main__':
    row = 4000
    x, y = dummy_data(row, 1)
    dates = pd.date_range('20190101', periods=row)
    df = pd.DataFrame(x, index=dates, columns=['X', 'Y'])  # 生成row行4列位置
 
    fig = px.density_heatmap(df, x="X", y="Y",
                             # rug(细条)、box(箱图)、violin(小提琴图)、histogram(直方图)。该参数用于在主图上方，绘制一个水平子图，以便对x分布，进行可视化.
                             marginal_x="rug",
                             marginal_y="histogram",
                             )
    fig.show()'''
 