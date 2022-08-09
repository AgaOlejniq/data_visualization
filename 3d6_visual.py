from itertools import count
from plotly.graph_objs import Bar, Layout
from plotly import offline

from unittest import result
from die import Die

d_6_1 = Die()
d_6_2 = Die()
d_6_3 = Die()

results = []

for roll in range(3, 1001):
    result = d_6_1.roll() + d_6_2.roll() + d_6_3.roll()
    results.append(result)

frequencies = []
max_result = d_6_1.num_sides * 3

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result', 'dtick' : 1}
y_axis_config = {'title' : 'Frequency of result'}
my_layout = Layout(title='Frequensies of results of rolling 3 D6 dice 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data' : data, 'layout' : my_layout}, filename='3xd6.html')