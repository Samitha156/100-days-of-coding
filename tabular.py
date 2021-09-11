# print("samitha")

# with open("weather_data.txt") as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
# 
# temp_list = data["temp"].to_list()
# print(temp_list)
# 
# sum_of_temp = sum(temp_list)
# average_temp = []
# #Average temperature
# # for temp in temp_list:
# #     average = round(temp / sum_of_temp, 2)
# #     average_temp.append(average)
# # print(average_temp)
# 
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# 
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# 
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday  = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp)*9/5 + 32)

data_dict = {
    "students": ["Amy", "James", "Sam"],
    "scores": [50, 65, 70]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

