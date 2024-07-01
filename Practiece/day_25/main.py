# import csv

# with open("weather_data.csv") as weather_file_data:
#     data = csv.reader(weather_file_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)

#     print(temperatures)     

# import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_average = sum(temp_list) / len(temp_list)
# print(temp_average)

# temp_mean = data["temp"].mean()
# print(temp_mean)

# # get Data in Columns
# print(data["condition"])
# print(data.condition)

# # get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,66,65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")





# ------------- Squirrel data ------------
# ----------------- 1 -----------
# import pandas

# data = pandas.read_csv("Park_Squirrel_Data.csv")

# fur_color = data["Primary Fur Color"].to_list()
# # print(fur_color)

# # Fur color count
# gray_squirrel = 0
# cinnamon_squirrel = 0
# black_squirrel = 0

# for color in fur_color:
#     if color == "Gray":
#         gray_squirrel += 1
#     elif color == "Cinnamon":
#         cinnamon_squirrel += 1
#     elif color == "Black":
#         black_squirrel += 1

# print(f"gray_squirrel = {gray_squirrel}\n cinnamon_squirrel = {cinnamon_squirrel}\n black_squirrel = {black_squirrel}")

# squirrel_color_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
# }

# data = pandas.DataFrame(squirrel_color_dict)
# data.to_csv("squirrel_color_data.csv")

# ----------------- 2 ---------------
import pandas

data = pandas.read_csv("Park_Squirrel_data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

squirrel_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

data = pandas.DataFrame(squirrel_color_dict)
data.to_csv("squirrel_color_data.csv")