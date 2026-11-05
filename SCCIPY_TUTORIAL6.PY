# HYPOTHESIS TESTING

# H0 IS NULL HYPO AND H1 IS ALTERNATIVE HYPO 
# IF P-VALUE <=0.5 REJECT H0
# AND P>0.05 REJECT TO FAIL H0
# P-VALUE IS THE PROBABLITY VALUE

# A company claims that the average time needed to pack an order is 30 minutes.A sample of 10 orders has the following packing times are 28,31,29,35,30,27,32,29,34 and 30 min.
# (i) At a 5% significance level
# (ii) Use a one-sample t-test to determine
# (iii) whether the actual packing time is significantly diff from the company claimed average

# h0 is 30 min and h1 is not 30
import numpy as np
from scipy import stats

time = np.array([28, 31, 29, 35, 30, 27, 32, 29, 34, 30])
t_stat,p_value=stats.ttest_1samp(time,popmean=30)

print("mean:",round(time.mean(),2))
print("t statistic:",round(t_stat,3))
print("p_value:",round(p_value,4))