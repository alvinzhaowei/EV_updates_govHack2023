import os
import pandas as pd
import pickle

data = {}
month_map = {"Jan": 1, "January": 1, "Feb": 2, "February": 2, "Mar": 3, "March": 3, "Apr": 4, "April": 4,
             "May": 5, "Jun": 6, "June": 6, "Jul": 7, "July": 7, "Aug": 8, "August": 8, "Sept": 9,
             "September": 9, "Oct": 10, "October": 10, "Nov": 11, "November": 11, "Dec": 12, "December": 12}
path_to_folder = "raw_data"
for file_name in os.listdir(path_to_folder):
    month, year = file_name.split(".")[0].split()[-2:]
    file_path = os.path.join(path_to_folder, file_name)
    dataFrame = pd.read_excel(file_path)
    year = int(year)
    month = month_map[month]
    data_np = dataFrame.values
    total_count = 0
    tesla_count = 0
    for row in data_np:
        if row[0] == 'TESLA ':
            tesla_count = row[1]
        if row[0] == 'Grand Total':
            total_count = row[1]
    if year not in data:
        data[year] = {}
        data[year][month] = (tesla_count, total_count)
    else:
        data[year][month] = (tesla_count, total_count)

pickle.dump(data, open("new_vehicles_by_month", "wb"))
