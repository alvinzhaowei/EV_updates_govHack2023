import numpy as np
import csv

vehicle_distribution = np.load("registered_vehicle_postcode.npy")
postcodes = sorted(list(set(vehicle_distribution[:, 3])))
data = np.zeros((len(postcodes), 49))
# each postcode is a row
# get the ev num and total cars each postcode
for i, postcode in enumerate(postcodes):
    data[i][0] = postcodes[i]
    data_postcode = vehicle_distribution[vehicle_distribution[:, 3] == postcode]
    v_num = np.sum(data_postcode[:, 4])
    data_postcode = data_postcode[data_postcode[:, 1] == 1]
    if len(data_postcode) == 0:
        ev_num = 0
    else:
        ev_num = np.sum(data_postcode[:, 4])
    data[i][47] = ev_num
    data[i][48] = v_num
# match for age data
csv_reader = csv.reader(open("raw_data/census/2021Census_G01_VIC_POA.csv"))
next(csv_reader)
max_total_people = 0
temp_total_people = {}
for line in csv_reader:
    postcode = int(line[0][3:])
    try:
        i = postcodes.index(postcode)
        total_male = int(line[1])
        total_female = int(line[2])
        total_people = int(line[3])
        temp_total_people[postcode] = total_people
        data[i][1] = total_male / total_people
        data[i][2] = total_female / total_people
        if total_people > max_total_people:
            max_total_people = total_people
        # age range
        z = 3
        for j in range(12, 37, 3):
            data[i][z] = line[j]
            z += 1
        # birth location
        data[i][12] = int(line[55]) / total_people
        data[i][13] = int(line[58]) / total_people
        # citizenship
        data[i][14] = int(line[68]) / total_people
        # students
        data[i][15] = int(line[77]) / total_people
        data[i][16] = int(line[80]) / total_people
        data[i][17] = int(line[83]) / total_people
        # education
        data[i][18] = int(line[86]) / total_people
        data[i][19] = int(line[89]) / total_people
        data[i][20] = int(line[92]) / total_people
        data[i][21] = int(line[95]) / total_people
        data[i][22] = int(line[98]) / total_people
        data[i][23] = int(line[101]) / total_people
    except ValueError:
        pass

# normalize the ev_num and v_num
for i, row in enumerate(data):
    postcode = int(row[0])
    try:
        total_people = temp_total_people[postcode]
        adjust_factor = total_people / max_total_people
        data[i][47] = data[i][47] / adjust_factor
        data[i][48] = data[i][48] / adjust_factor
    except KeyError:
        pass

max_ev_num = np.max(data[:, 47])
max_v_num = np.max(data[:, 48])
data[:, 47] = data[:, 47] / max_ev_num
data[:, 48] = data[:, 48] / max_v_num

# match for income
csv_reader = csv.reader(open("raw_data/census/2021Census_G02_VIC_POA.csv"))
next(csv_reader)
max_m_personal_income = 0
max_m_mortgage = 0
max_m_rent_weekly = 0
max_m_household_income = 0
for line in csv_reader:
    postcode = int(line[0][3:])
    try:
        i = postcodes.index(postcode)
        mortgage = int(line[2])
        income = int(line[3])
        rent = int(line[4])
        household = int(line[7])
        data[i][24] = mortgage
        data[i][25] = income
        data[i][26] = rent
        data[i][27] = household
        if mortgage > max_m_mortgage:
            max_m_mortgage = mortgage
        if income > max_m_personal_income:
            max_m_personal_income = income
        if rent > max_m_rent_weekly:
            max_m_rent_weekly = rent
        if household > max_m_household_income:
            max_m_household_income = household
    except ValueError:
        pass

# normalize money
for i, row in enumerate(data):
    try:
        postcode = int(row[0])
        data[i][24] = data[i][24] / max_m_mortgage
        data[i][25] = data[i][25] / max_m_personal_income
        data[i][26] = data[i][26] / max_m_rent_weekly
        data[i][27] = data[i][27] / max_m_household_income
    except KeyError:
        pass

# match for marriage
csv_reader = csv.reader(open("raw_data/census/2021Census_G06_VIC_POA.csv"))
next(csv_reader)
for line in csv_reader:
    postcode = int(line[0][3:])
    try:
        i = postcodes.index(postcode)
        m_not_married = int(line[39])
        f_not_married = int(line[79])
        total_not_married = m_not_married + f_not_married
        total_people = temp_total_people[postcode]
        data[i][28] = m_not_married / total_people
        data[i][29] = f_not_married / total_people
        data[i][30] = total_not_married / total_people
    except ValueError:
        pass

# match for occupation
csv_reader = csv.reader(open("raw_data/census/2021Census_G60A_VIC_POA.csv"))
next(csv_reader)
for line in csv_reader:
    postcode = int(line[0][3:])
    try:
        i = postcodes.index(postcode)
        total_people = temp_total_people[postcode]
        data[i][31:39] = [int(digit) / total_people for digit in line[91:99]]
        data[i][39:47] = [int(digit) / total_people for digit in line[191:199]]
    except ValueError:
        pass
data = data[data[:, 1] > 0]
print(data)
np.save("ev_census_data", data)
