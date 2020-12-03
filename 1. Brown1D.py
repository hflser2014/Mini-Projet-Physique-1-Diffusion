import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

locsList = []
n = 10000
t = 5000

locs = np.zeros((n, 1), dtype=int)
for i in range(t):
    locs += np.random.randint(-1, 2, locs.shape)
    locsList.append(locs.copy())

ylist = np.array(locsList).T[0]
'''
for ay in ylist: 
    plt.plot(range(len(ay)),ay)
plt.show()
'''
yu = ylist[:,-1]
yu.sort()

print(yu)

plt.plot(range(len(yu)),yu)
plt.show()

mu =np.mean(yu) #计算均值 
sigma =np.std(yu) 
num_bins = 50 #直方图柱子的数量 
n, bins, patches = plt.hist(yu, num_bins,density=1, alpha=0.75) 
#直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的yu值，及各个方块对象 

y = norm.pdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y 
 
plt.grid(True)
plt.plot(bins, y, 'r--') #绘制y的曲线 
plt.xlabel('values') #绘制x轴 
plt.ylabel('Probability') #绘制y轴 
plt.title('Histogram : $\mu$=' + str(round(mu,2)) + ' $\sigma=$'+str(round(sigma,2)))  #中文标题 u'yuyuyu' 
#plt.subplots_adjust(left=0.15)#左边距 
plt.show()
