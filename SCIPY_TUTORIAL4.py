# A SUPPORT DESK AVERAGES 4 TICKETS PER HOUR
# (i) FIND PROB OF EXACTLY 6 TICKETS IN NEXT HOUR

from scipy.stats import poisson
# poisson = poisson distribution
lam=4
k=6
# lam = lambda
prob=poisson.pmf(k,lam)
print(round(prob,4))
print("At most 6 :", round(poisson.cdf(6,lam),4))