import matplotlib.pyplot as plt
import numpy as np

data = np.load("ev_census_data.npy")

y = data[:, 47]
line = []
y_data = []
feature_names = ["male percentage", "female percentage", "15_19", "20_24", "25_34", "35_44", "45_54",
                 "55_64", "65_74", "75_84", "85+", "born in Aus", "born \n elsewhere", "citizen",
                 "student 15_19", "student 20_24", "student 25+", "completed \n year 12", "completed \n year 11",
                 "completed \n year 10", "completed \n year 9", "completed \n year 8", "Did not go to school",
                 "mortgage \n repayment", "median income", "rent cost", "median household income",
                 "male not married", "female not married", "total not married",
                 "MALES_Occupation_Managers",
                 "male \n Professionals",
                 "MALES_Technicians_and_trades_workers",
                 "MALES_Community_and_personal_service_workers",
                 "MALES_Clerical_and_administrative_workers",
                 "MALES_Sales_workers",
                 "MALES_Machinery_operators_and_drivers",
                 "male \n Labourers",
                 "FEMALES_Managers",
                 "FEMALES_Professionals",
                 "FEMALES_Technicians_and_trades_workers",
                 "FEMALES_Community_and_personal_service_workers",
                 "FEMALES_Clerical_and_administrative_workers",
                 "FEMALES_Sales_workers",
                 "FEMALES_Machinery_operators_and_drivers",
                 "FEMALES_Labourers",
                 "EVs registered"
                 ]

for i in range(1, 47):
    x = data[:, i]
    r = np.corrcoef(x, y)
    cc = r[0, 1]
    y_data.append(cc)

sorted_index = list(reversed(np.argsort(y_data)))

x_ticks = []
new_y_data = []
font = {'size': 15}
plt.rc('font', **font)
plt.figure(figsize=(20, 6))
for i in sorted_index[:5]:
    x_ticks.append(feature_names[i])
    new_y_data.append(y_data[i])
for i in sorted_index[-5:]:
    x_ticks.append(feature_names[i])
    new_y_data.append(y_data[i])
plt.figure(figsize=(20, 6))
plt.bar(x_ticks, new_y_data,
        color=['tab:blue', 'tab:blue', 'tab:blue', 'tab:blue', 'tab:blue',
               'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red'])
plt.savefig("figures/top5.png")
