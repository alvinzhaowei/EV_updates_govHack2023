import numpy as np
import matplotlib.pyplot as plt

data = np.load("registered_vehicle_postcode.npy")
data = data[data[:, 3] >= 3000]
data = data[data[:, 3] <= 3999]
total_cars = np.sum(data[:, 4])
data = data[data[:, 1] == 1]
EV_cars = np.sum(data[:, 4])
print(total_cars)
print(EV_cars)

print(EV_cars / total_cars)

years = set(data[:, 2])
years = sorted(list(years))
counts = []
for year in years:
    temp_data = data[data[:, 2] == year]
    count = np.sum(temp_data[temp_data[:, 0] == 1085][:, 4])
    count1 = np.sum(temp_data[:, 4])
    # print(count1)
    # print(count)
    counts.append(count)

plt.bar(years[-6:], counts[-6:])
plt.xlabel("EV still using by manufacture year")
plt.show()
