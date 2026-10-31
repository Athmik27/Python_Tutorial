import matplotlib.pyplot as plt

months=["JAN",'FEB','MAR','APR']
sales=[100,150,70,75]

plt.figure(figsize=(10,6))
bars=plt.bar(months,sales,color='lightblue',linewidth=0.5)

for bar in bars :
    plt.text(bar.get_x()+ bar.get_width()/2,
            bar.get_height()+3,
            f"{bar.get_height()}",
            ha='center',
            fontsize=11,
            fontweight='bold')


plt.xlabel("MONTHS")
plt.ylabel("SALES")
plt.title("month sales board")

plt.grid(axis='y',linestyle="--",alpha=0.5)
plt.show()