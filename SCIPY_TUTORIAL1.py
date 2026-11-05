# A CUSTOMER CALL CENTER RECIVES AN AVERAGE OF 4 CALLS PER MIN.
# (i) prob of getting exactly 2 calls
# (ii) prob of getting at most 2 calls
# (iii) prob of getting more than 2 calls

from scipy.stats import poisson
# poisson = poisson distribution
lam=4
# lam = lambda
print("Exactly 2 calls:",poisson.pmf(2,lam)) # pmf is for exactly
print("At most 2 calls:",poisson.cdf(2,lam)) # cdf is for upto
print("More than 2 calls:",poisson.sf(2,lam)) # sf is for above


