import matplotlib.pyplot as plt
import numpy as np

data = np.load("ev_census_data.npy")

y = data[:, 47]
line = []
y_data = []

# (1-3)
# x_ticks = ["Male",
#            "Female"]

# (3-12)
# x_ticks = ["15-19", "20-24", "25-34", "35-44", "45-54",
#            "55-64", "65-74", "75-84", "85+"]

# (12-15)
# x_ticks = ["Born in Aus", "Born elsewhere", "citizen"]

# (15-18)
# x_ticks = ["student 15-19", "student 20-24", "student 25+"]

# (18-24) reversely
# x_ticks = ["Did not \n go to school", "completed \n year 8", "completed \n year 9",
#            "completed \n year 10", "completed \n year 11", "completed \n year 12"]

# (24-28)
x_ticks = ["mortgage \n repayment", "rent cost", "personal income", "household income"]

# (28-31)
# x_ticks = ["male not married", "female not married", "total not married"]

# male: (31-39), female:(39-47)
# x_ticks = ["Managers",
#            "Professionals",
#            "Technicians and \n trades",
#            "Community and \n personal service",
#            "Clerical and \n administrative",
#            "Sales",
#            "Machinery operators \n and drivers",
#            "Labourers", ]

for i in range(24, 28):
    x = data[:, i]
    r = np.corrcoef(x, y)
    cc = r[0, 1]
    y_data.append(cc)

# font = {'size': 15}
# plt.rc('font', **font)
# plt.figure(figsize=(20, 6))

# swap the cc as we change the order for income
temp = y_data[1]
y_data[1] = y_data[2]
y_data[2] = temp

plt.bar(x_ticks, y_data,
        color=['tab:blue', 'tab:blue', 'tab:blue', 'tab:blue', 'tab:red',
               'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red'])

plt.savefig("figures/income_cost.png")
