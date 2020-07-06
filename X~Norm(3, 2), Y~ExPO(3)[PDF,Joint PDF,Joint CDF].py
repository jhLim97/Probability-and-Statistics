from scipy.stats import norm
from scipy.stats import expon
import math

y1 = norm.pdf(1.0,3,math.sqrt(2))
y2 = expon.pdf(1,0,1/3)
y3 = norm.cdf(1.0,3,math.sqrt(2))
y4 = expon.cdf(1,0,1/3)

print(y1,y2) #PDF: fx(1.0) for X, and fY(1) for Y 
print(y1*y2) #Joint PDF:  fx,Y(1.0, 1.0)
print(y3*y4) #Joint CDF:  Fx,Y(1.0, 1.0)
