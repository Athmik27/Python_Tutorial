# A TEAM INSEPECTS THE 20 INDEPENDENT ITEMS AND EACH HAS 5% OF DEFECT PROBABLITY
# (i) PROB OF EXACTLY 2 DEFECT

from scipy.stats import binom
# binom = binomial distribution
n=20
p=0.05
k=2
prob=binom.pmf(k,n,p)
print(round(prob,4))
print("At most 2 defects:",binom.cdf(2,n,p))
print("More than 2 defects:",binom.sf(2,n,p))