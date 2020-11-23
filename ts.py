import tushare as ts
import matplotlib.pyplot as plt
import numpy as np

def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

df = ts.get_k_data('510300')#沪深300股票

close =np.array(df.close)
ln_close = np.log(close)
r = [ln_close[i+1]-ln_close[i] for i in range(0,len(ln_close)-1)]
r= np.array(r)

mean = r.mean()
std = r.std()
x_max = r.max()
x_min = r.min()

x = np.arange(x_min, x_max, 0.001)
y = normfun(x, mean, std)
plt.xlim(x_min, x_max)
plt.hist(r, bins=int(np.sqrt(len(r))), rwidth=0.9, density=True)
plt.plot(x, y)
plt.show()