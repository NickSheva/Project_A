# Create a graph pie

import matplotlib.pyplot as plt

sales = [950000, 650000, 450000, 1600000, 60000, 40000,
         3500000, 100000, 60000, 500000]
labels = ["Rolex", "Omega", "Cartier", "Longines", "Patek Philippe",
          "Audemars Piguet", "Tissot", "IWC", "Hublot", "TAG Heuer", ]


fig, ax = plt.subplots()
ax.pie(sales, labels=labels)


plt.show()
