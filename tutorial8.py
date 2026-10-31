import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
salary=np.random.normal(5000,6000,7000)

plt.figure(figsize=(10,6))
plt.hist(salary,bins=20,color='lightblue',edgecolor='black',alpha=0.5)

plt.xlabel("salary")
plt.ylabel("frequency")
plt.title("salary distribution")

plt.show()