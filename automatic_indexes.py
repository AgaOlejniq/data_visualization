import csv
from datetime import datetime
from shutil import which
import matplotlib.pyplot as plt


def get_weather_data(filename, dates, highs, lows):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column in enumerate(header_row):
            print(index, column)

        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        
        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
                
            except ValueError:
                print(f"missing data for {date}")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
                
# get data 
filename = 'python_crash_course\part_2\data_visualization\excersises\data\sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows)

# plot
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# format
title = f'Daily weather in Sitka, 2018'
plt.title(title, fontsize= 24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures [F]', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()