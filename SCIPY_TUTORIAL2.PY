#  A COMP FINDS THAT THE PROB OF CUSTOMER PURCHASING A PROD IS 0.5.IF 5 CUSTOMER AS SELECTED THEN FIND
# (i) prob of getting exactly 3 PROD PURCHASE
# (ii) prob of getting at most 3
# (iii) prob of getting more than 3

from scipy.stats import binom
# binom = binomial distribution
n=5
p=0.6
print("Exactly 2 customers:",binom.pmf(3,n,p)) # pmf is for exactly
print("At most 2 customers:",binom.cdf(3,n,p)) # cdf is for upto
print("More than 2 customers:",binom.sf(3,n,p)) # sf is for above