#   CONTINIOUS DISTRIBUTION 

# An Package delivery time has mean of 40 min and sd of 5 min,what proportion takes under 47 minutes.

from scipy.stats import norm
# here norm is normal distribution

mu,sigma,x=40,5,47
z=(x-mu)/sigma
p_under=norm.cdf(x,loc=mu,scale=sigma)

print("z-score:",round(z,2))
print("P(time<=47):",round(p_under,4))

