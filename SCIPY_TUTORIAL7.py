# DECISION RULE :

# IF P<0.05 EVIDANCE IS INSUFFICIENT WITH NULL MEAN AT THRESHOLD.
# IF P>=0.05 THEN THE INSUFFICIENT EVIDENCE TO REJECT IT NOT PROOF THAT IT MEANS ARE EQUAL.
 
 # CHI SQUARE DISTRIBUTION AND TESTS
# used to check dependent / independent variable.this uses goodness of fit for categories and variables.
# x square=summation (observed frequency and expected frequency )square divided by expeected frequency.

# A COMPANY HAS RECORDED THE CUSTOMERS ARE ACRPSS FOUR CATEGORIES.
# the observed complaints counts are 18,22,27,33. if complaints are expected to be distributed equally across all 4 categories counts are expected counts statistically significant.


from scipy.stats import chisquare
observed =[18,22,27,33]
result = chisquare(observed)
print("chi-square:",round(result.statistic,3))
print("p_value:",round(result.pvalue,4))

# p-value=0.1689
# significance level =0.05
# as 0.1689 > 0.05 the hypothesis is failed
