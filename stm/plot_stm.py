import parse_plot2d
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

rootdir = "/home1/srigamonti/projects/stm/runs/97/"
r, rl, func = parse_plot2d.parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")

nx = len(r)
ny = len(r[0])

x=[]
y=[]
#f=[]
for i in range(nx):
    x.append([])
    y.append([])
#    f.append([])
    for j in range(ny):
        x[i].append(r[i][j][0])
        y[i].append(r[i][j][1])
#        f[i].append(func[i][j])

# Make plot

fig=plt.figure(1,figsize=(8,5.5))

params = {'font.size':15,
          'xtick.major.size': 5,
          'ytick.major.size': 5,
          'patch.linewidth': 1.5,
          'axes.linewidth': 2.,
          'axes.formatter.limits': (-4, 6),
          'lines.linewidth': 1.8,
          'lines.markeredgewidth':2.0,
          'lines.markersize':18,
          'legend.fontsize':11,
          'legend.borderaxespad':1,
          'legend.borderpad':0.5,
          'savefig.dpi':80}

plt.rcParams.update(params)