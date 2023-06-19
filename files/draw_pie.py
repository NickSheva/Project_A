# Create a graph pie

import matplotlib.pyplot as plt

sales = [950000, 650000, 450000, 1600000, 60000, 40000,
         3500000, 100000, 60000, 500000]
labels = ["Rolex", "Omega", "Cartier", "Longines", "Patek Philippe",
          "Audemars Piguet", "Tissot", "IWC", "Hublot", "TAG Heuer", ]
explode = [0.1, 0, 0, 0, 0.2, 0, 0, 0.1, 0, 0]


fig, ax = plt.subplots()
ax.pie(sales, labels=labels, explode=explode, shadow=True, startangle=150, autopct="%1.1f%%")
ax.axis("equal")

plt.show()
