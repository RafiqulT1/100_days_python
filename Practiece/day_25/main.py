import csv

with open("weather_data.csv") as weather_file_data:
    data = csv.reader(weather_file_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperature = int(row[1])
            temperatures.append(temperature)

    print(temperatures)     
