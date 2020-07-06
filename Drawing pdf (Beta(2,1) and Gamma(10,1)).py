import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import gamma
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(0,1,100)
y=np.linspace(0,30,100)

plt.plot(x,beta.pdf(x,2,1))
plt.show() #PDF: fx(x) for X

fig=plt.figure()
ax=fig.gca(projection='3d')
x,y=np.meshgrid(x,y)
ax.plot_surface(x,y,beta.pdf(x,2,1)*gamma.pdf(y,10,1))
plt.show() #Joint PDF: fx,Y (x,y)
