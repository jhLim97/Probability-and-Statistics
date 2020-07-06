import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

plt.plot(x,norm.pdf(x,0,1),'r')
plt.show() #PDF: fx(x) for X

fig=plt.figure()
ax=fig.gca(projection='3d')
x,y=np.meshgrid(x,y)
ax.plot_surface(x,y,norm.pdf(x,0,1)*norm.pdf(y,0,1))
plt.show() #Joint PDF: fx,Y (x,y)
