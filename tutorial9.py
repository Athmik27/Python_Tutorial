import matplotlib.pyplot as plt

months=["JAN",'FEB','MAR','APR']
sales=[100,150,70,75]

plt.figure(figsize=(10,6))
plt.scatter(months,sales,color='blue',marker='o',linewidth=0.5)

for i in range(len(months)):
    plt.text(months[i],sales[i]+2,sales[i],ha='center')


plt.xlabel("MONTHS")
plt.ylabel("SALES")
plt.title("Month Sales Board")

plt.grid(True)
plt.show()
