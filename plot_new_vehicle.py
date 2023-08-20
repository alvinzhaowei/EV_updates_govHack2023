import matplotlib.pyplot as plt
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

data = pickle.load(open("new_vehicles_by_month", "rb"))
years = [year for year in range(2018, 2023)]

y1 = []
y2 = []
y = []
x_ticks = []
for year in years:
    year_count = 0
    for month in range(1, 13):
        if month not in data[year]:
            continue
        else:
            # x_ticks.append(str(year) + "_" + str(month))
            # y1.append(data[year][month][1])
            # y2.append(data[year][month][0])
            year_count += data[year][month][0]
    x_ticks.append(year)
    y.append(year_count)

# adjusting factors (2018 only one month data, 2022 only 6 months data)
y[0] = y[0] * 12
y[-1] = y[-1] * 2

plt.bar(x_ticks, y)
changes = [""]
changes.extend([(y[i] - y[i - 1]) / y[i - 1] for i in range(1, len(y))])
for i in range(1, len(changes)):
    change = changes[i] * 100
    change = "%.0f" % change
    change += "%"
    changes[i] = change
print(changes)
for i, v in enumerate(y):
    plt.text(x_ticks[i] - 0.2, v + 40, changes[i], fontsize=10)
plt.plot(x_ticks, y, color='tab:red')

# plt.show()
plt.savefig("figures/total_new_tesla_each_year.png")
