import csv
import pickle
import numpy as np

id_manName = {}
manName_id = {}
csv_reader = csv.reader(open("Whole_Fleet_Vehicle_Registration_Snapshot_by_Postcode_Q2_2023.csv", encoding="utf-8"))
header = next(csv_reader)
id_count = 0
data = []
for i, line in enumerate(csv_reader):
    entry = [0, 0, 0, 0, 0]
    if len(line) == 0:
        continue
    vehicle_make = line[0]
    vehicle_class = line[1]
    fuel_type = line[4]
    if fuel_type == 'E ':
        fuel_type = 1
    else:
        fuel_type = 0
    postcode = line[3]
    manufacture_year = line[2]
    count = line[5]
    if vehicle_make not in manName_id:
        manName_id[vehicle_make] = id_count
        id_manName[id_count] = vehicle_make
        entry[0] = id_count
        id_count += 1
    else:
        entry[0] = manName_id[vehicle_make]
    entry[1] = fuel_type
    entry[2] = int(manufacture_year)
    entry[3] = int(postcode)
    entry[4] = int(count)
    data.append(entry)
data = np.array(data)
pickle.dump(manName_id, open("manName_id", "wb"))
pickle.dump(id_manName, open("id_manName", "wb"))
print(manName_id['TESLA '])
np.save("registered_vehicle_postcode", data)
