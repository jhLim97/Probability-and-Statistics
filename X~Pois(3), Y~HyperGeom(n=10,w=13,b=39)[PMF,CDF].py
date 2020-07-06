from scipy.stats import poisson
from scipy.stats import hypergeom
x1 = poisson(3).pmf(7) #pmf of poisson in X=7
x2 = poisson(3).cdf(7) #cdf of poisson in X=7
x3 = poisson(3).cdf(9) #cdf of poisson in X=9
hpd = hypergeom(52,13,10)
pmf_hpd = hpd.pmf(5) #pmf of hypergeom in Y=5
cdf_hpd1 = hpd.cdf(5) #cdf of hypergeom in Y=5
cdf_hpd2 = hpd.cdf(9) #cdf of hypergeom in Y=9
result1 = x3-x2 #poisson in 7<X<=9
result2 = cdf_hpd2-cdf_hpd1 #hypergeom in 5<Y<=9
print(x1) #pmf of poisson in X=7
print(pmf_hpd) #pmf of hypergeom in Y=5
print(x2) #cdf of poisson in X=7
print(cdf_hpd1) #cdf of hypergeom in Y=5
print(result1) #poisson in 7<X<=9
print(result2) #hypergeom in 5<Y<=9
