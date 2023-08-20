import numpy as np
import csv

csv_writer = csv.writer(open("cc.csv", "w", newline=''))
data = np.load("ev_census_data.npy")
feature_names = ["male percentage", "female percentage", "15_19", "20_24", "25_34", "35_44", "45_54",
                 "55_64", "65_74", "75_84", "85+", "Born in Aus", "Born elsewhere", "citizen",
                 "student 15_19", "student 20_24", "student 25+", "completed year 12", "completed year 11",
                 "completed year 10", "completed year 9", "completed year 8", "Did not go to school",
                 "median mortgage repayment", "median income", "median rent", "median household income",
                 "male not married", "female not married", "total not married",
                 "MALES_Occupation_Managers",
                 "MALES_Occupation_Professionals",
                 "MALES_Technicians_and_trades_workers",
                 "MALES_Community_and_personal_service_workers",
                 "MALES_Clerical_and_administrative_workers",
                 "MALES_Sales_workers",
                 "MALES_Machinery_operators_and_drivers",
                 "MALES_Labourers",
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
csv_writer.writerow(["feature name", "cc"])
y = data[:, 47]
line = []
for i in range(1, 48):
    x = data[:, i]
    r = np.corrcoef(x, y)
    line = [feature_names[i - 1], r[0, 1]]
    csv_writer.writerow(line)
