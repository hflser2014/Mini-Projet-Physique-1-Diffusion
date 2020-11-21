import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from scipy import stats
from scipy import constants
import adjLine

# (Square) grid side length.
m = 50
# Maximum numbter of iterations.
nitmax = 200
# Number of particles in the simulation.
nparticles = 5000
# Output a frame (plot image) every nevery iterations.
nevery = 2
# Constant maximum value of z-axis value for plots.
zmax = 30

# Create the 3D figure object.
fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
p1 = fig.add_subplot(221, projection='3d')
p2 = fig.add_subplot(222)
p3 = fig.add_subplot(223)
p4 = fig.add_subplot(224)

# We'll need a meshgrid to plot the surface: this is X, Y.
x = y = np.linspace(1, m, m)
X, Y = np.meshgrid(x, y)

# vmin, vmax set the minimum and maximum values for the colormap. This is to
# be fixed for all plots, so define a suitable norm.
vmin, vmax = 0, zmax
norm = colors.Normalize(vmin=vmin, vmax=vmax)

# Initialize the location of all the particles to the centre of the grid.
locs = np.ones((nparticles, 2), dtype=int) * m//2
disArray = []
disArrayMean = []
listVariance = []
locsArray = []


def calcEntropy(locs):
    coor = np.stack(locs, axis=0)
    x = coor[0]
    y = coor[1]

    # Define the borders
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY
    # print(xmin, xmax, ymin, ymax)
    # Create meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j,
                      ymin:ymax:100j]

    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = stats.gaussian_kde(values)
    pdistribute = np.reshape(
        kernel(positions).T, xx.shape)

    frame = pdistribute

    mean = np.mean(frame, axis=0)
    mean = np.mean(mean, axis=0)
    Variance = 0
    for i1 in frame:
        for i2 in i1:
            Variance -= constants.k*i2*np.log(i2)
    return Variance

    # listVariance.append(Variance)


# Iterate for nitmax cycles.
for j in range(nitmax):
    # Update the particles' locations at random. Particles move at random to
    # an adjacent grid cell. We're going to be pretty relaxed about the ~11%
    # probability that a particle doesn't move at all (displacement of (0,0)).
    locs += np.random.randint(-1, 2, locs.shape)
    #locs = np.where()

    disArray.append([])
    if not (j+1) % nevery:
        # Create an updated grid and plot it.
        grid = np.zeros((m, m))
        Variance = 0
        for i in range(nparticles):
            x, y = locs[i]

            dis = np.sqrt((x-m//2)**2+(y-m//2)**2)
            disArray[-1].append(dis)

            # Add a particle to the grid if it is actually on the grid!
            if 0 <= x < m and 0 <= y < m:
                grid[x, y] += 1

        '''
        # calculate the variance of the system
        mean = np.mean(np.mean(grid))
        for i1 in grid:
            for i2 in i1:
                Variance = Variance + (i2-mean)**2
        Variance /= x*y
        listVariance.append(Variance)
        '''

        print(j+1, '/', nitmax)

        disArrayMean.append(np.mean(np.array(disArray[-1])))  # 计算平均速度
        locsArray.append(locs.T.copy())
        listVariance.append(calcEntropy(locs.T))

        # Now clear the Axes of any previous plot and make a new surface plot.
        p1.clear()
        p2.clear()
        p3.clear()
        p4.clear()

        p1.set_title("分布密度图象")
        p1.plot_surface(X, Y, grid, rstride=1, cstride=1, cmap=plt.cm.autumn,
                        linewidth=1, vmin=vmin, vmax=vmax, norm=norm)
        p1.set_zlim(0, zmax)
        # Save to 'diff-000.png', 'diff-001.png', ...
        # plt.savefig('diff-{:03d}.png'.format(j//nevery))

        p2.set_title("二维扩散图象")
        p2.set_xlim(0, m)
        p2.set_ylim(0, m)
        p2.scatter(locs.T[0], locs.T[1], color="royalblue")

        p3.set_title("平均位移关于时间变化图象")
        p3.plot(range(len(disArrayMean)), disArrayMean, color="red")

        p4.set_title("熵关于时间变化图象")
        p4.plot(range(len(listVariance)), listVariance, color="royalblue")

        plt.pause(0.000001)

p1.clear()
p2.clear()
p3.clear()
p4.clear()
adjLine.output(range(len(disArrayMean)), disArrayMean)
