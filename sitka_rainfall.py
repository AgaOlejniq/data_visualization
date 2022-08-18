import csv
from datetime import datetime
from turtle import width
import matplotlib.pyplot as plt

filename = 'python_crash_course\part_2\data_visualization\excersises\data\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column in enumerate(header_row):
        print(index, column)

    # Get dates, precipitation.
    dates, precipitations = [], []

    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[3])
        except ValueError:
            print(f'-missing data for {date}')
        else:
            dates.append(date)
            precipitations.append(precipitation)

# Plot
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='blue', alpha=0.5)

# Format
title = 'Daily precipitations in Sitka, Alaska, 2018'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation [in]', fontsize=16)
ax.tick_params(axis='both', labelsize=16)

plt.show()
