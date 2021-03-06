#!/usr/bin/python
import parse_plot2d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm # color map library
import os
import sys

args = sys.argv[1:]

if "-tile" in args:
    ind = args.index("-tile")
    ti = int(args[ind+1]) 
    tj = int(args[ind+2]) 
else:
    ti = 1
    tj = 1
    
if "-skip" in args:
    ind = args.index("-skip")
    skip = int(args[ind+1]) 
else:
    skip = 1

r, rl, basevect, func = parse_plot2d.parse_plot2d("input.xml", "STM2d2D.XML")

bohrToAng = 0.529177249

ni0 = len(r)
nj0 = len(r[0])
ni = int(round(ti * ni0 / skip))
nj = int(round(tj * nj0 / skip))
x=[]
y=[]
f=[]
for i in range(ni):
    x.append([])
    y.append([])
    f.append([])
    it = np.mod(i*skip,ni0)
    itf = int(i*skip/(ni0))
    for j in range(nj):
        jt = np.mod(j*skip,nj0)
        jtf = int(j*skip/(nj0))
        dx = basevect[0][0]*itf+basevect[1][0]*jtf
        dy = basevect[0][1]*itf+basevect[1][1]*jtf
        xt = r[it][jt][0]+dx
        yt = r[it][jt][1]+dy
        x[i].append(xt * bohrToAng)
        y[i].append(yt * bohrToAng)
        f[i].append(func[it][jt])
xnp=np.array(x)
ynp=np.array(y)
fnp=np.array(f)

# Make plot
gray=1.00

cdict = {'red':   ((0.0,  gray, gray),
                   (1.0,  0.35, 0.35)),

         'green': ((0.0,  gray, gray),
                   (1.0,  0.5, 0.5)),

         'blue':  ((0.0,  gray, gray),
                   (1.0,  0.8, 0.8))}

white_red = LinearSegmentedColormap('whiteRed', cdict)


fig=plt.figure(1,figsize=(8.0,8.0))

params = {'font.size':15,
          'xtick.major.size': 5,
          'ytick.major.size': 5,
          'patch.linewidth': 1.5,
          'axes.linewidth': 2.,
          'axes.formatter.limits': (-4, 6),
          'lines.linewidth': 1.0,
          'lines.markeredgewidth':2.0,
          'lines.markersize':18,
          'legend.fontsize':11,
          'legend.borderaxespad':1,
          'legend.borderpad':0.5,
          'savefig.dpi':80}

plt.rcParams.update(params)
ax=fig.add_subplot(111, aspect='equal')

ax.pcolor(xnp,ynp,fnp,cmap=cm.copper)

ax.set_xlabel("$\AA$")
ax.set_ylabel("$\AA$")

if "-png" in args:
    plt.savefig('PLOT.png', orientation='portrait',format='png')
else:
    plt.show()












