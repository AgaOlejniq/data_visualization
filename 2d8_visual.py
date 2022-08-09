from itertools import count
from plotly.graph_objs import Bar, Layout
from plotly import offline

from unittest import result
from die import Die

die1 = Die(8)
die2 = Die(8)

results = []

for num_roll in range(2, 10001):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result', 'dtick' : 1}
y_axis_config = {'title' : 'Frequency of result'}
layout = Layout(title='Frequencies of results of rolling 2 D8 10 000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data' : data, 'layout' : layout}, filename='2xd8.html')