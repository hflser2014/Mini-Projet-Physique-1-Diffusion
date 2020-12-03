from scipy.stats import norm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab 
import math
import scipy.stats as stats


'''15 
16 
17 几何布朗运动:
18     St=S0*exp(ut)
19     St=S0*exp(u t+o e sqrt(dt))
20     
21     St=S0*exp(a t+b z)
22 
23 '''
D=250*4   #250个交易日每天四小时
T=5.0   #总时间1年
dt=T/D   #单位时间

s0=100   #初始价格
i=2
st=np.zeros((i,D))
st[0]=s0
a=0.15
b=0.3
n=round(T/dt)#dimension
ax=plt.subplot(211)
L=[]
for g in range(1, i):
    t=np.linspace(0,T,n)
    e=np.random.standard_normal(size=n)
    z=np.cumsum(e)*np.sqrt(dt)
    x=a*t+b*z
    st[g]=st[0]*np.exp(z)    
    plt.plot(t,st[g],label='st'+str(g))
    L.append(st[g])
'''    # 均值
u = 0
    #标准差 
sig = math.sqrt(dt)
ax=plt.subplot(212)
x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2) / (math.sqrt(2 * math.pi) * sig))
plt.plot(x,y_sig,"r-",linewidth=2)
plt.grid(True)'''
#画散点图和直方图
ax = plt.figure(figsize = (10,6))
'''ax1 = fig.add_subplot(3,1,2)  # 创建子图1
ax1.scatter(s.index, s.values)
plt.grid()'''

ax = plt.subplot(212)  # 创建子图2
for i in range(len(L)):
    plt.hist(L[i])
    plt.plot(kde=True)                         
    # 绘制拟合的正态分布图
    M_S = stats.norm.fit(L[i]) 
    normalDistribution = stats.norm(M_S[0], M_S[1]) 
    x = np.linspace(0,L[i],100)
    plt.plot(x, normalDistribution.pdf(x), c='orange')
plt.show()
     


#plt.legend()
plt.show()
plt.show() 