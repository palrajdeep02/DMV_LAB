import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]


plt.pie(sizes, labels=labels)


plt.title("Static Pie Chart")


plt.show()