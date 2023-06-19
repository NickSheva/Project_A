# Create a graph pie

import matplotlib.pyplot as plt

sales = [950000, 650000, 450000, 1600000, 60000, 40000,
         3500000, 100000, 60000, 500000]
labels = ["Rolex", "Omega", "Cartier", "Longines", "Patek Philippe",
          "Audemars Piguet", "Tissot", "IWC", "Hublot", "TAG Heuer"]
explode = [0.1, 0, 0, 0, 0.2, 0, 0, 0.1, 0, 0]
colors = ["green", "cyan", "lightyellow", "red", "yellow", "pink",
          "lightgray", "Lightblue", "lightgreen", "orange"]

fig, ax = plt.subplots()
ax.pie(sales, labels=labels, explode=explode, colors=colors, shadow=True,
       startangle=150, autopct="%1.1f%%")
patches, texts, auto = ax.pie(sales, labels=labels, explode=explode, colors=colors, shadow=True,
                              startangle=150, autopct="%1.1f%%")

plt.legend(patches, labels, loc=(1, 0.5))  # bbox_to_anchor=(0.85, 1.15))
plt.title("WATCHES  2022", fontweight='bold')
ax.axis("off")

plt.show()
