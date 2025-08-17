"""
=====================
Whats New 1 Subplot3d
=====================

"""
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import sys
num=301
min = -2
max = 2
X = np.arange(0, num, 1)
Y = np.arange(0, num, 1)
X, Y = np.meshgrid(X, Y)
file=open("VBM",'r+')
Z=file.readlines()
Z=[Z[i].strip().split() for i in range(len(Z))]
Z=[float(Z[i][0]) for i in range(len(Z))]
Z=np.array(Z)
Z.resize(num,num)
file2=open("CBM",'r+')
Z2=file2.readlines()
Z2=[Z2[i].strip().split() for i in range(len(Z2))]
Z2=[float(Z2[i][0]) for i in range(len(Z2))]
Z2=np.array(Z2)
Z2.resize(num,num)
#####################
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_surface(Y,X, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_xlim3d(0.0, num)
ax.set_ylim3d(0.0, num)
ax.set_zlim3d(min, max)

#fig.colorbar(surf, shrink=0.2, aspect=10)
surf2 = ax.plot_surface(Y,X, Z2, rstride=1, cstride=1, cmap=cm.RdYlGn,
        linewidth=0, antialiased=False)
ax.set_xticks([])
ax.set_yticks([])
#fig.colorbar(surf2, shrink=0.2, aspect=10)
#####################
ax.view_init(elev=5,azim=30)
plt.savefig("3d.png",dpi=600)

