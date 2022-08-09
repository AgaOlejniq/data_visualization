from itertools import count
from plotly.graph_objs import Bar, Layout
from plotly import offline

from unittest import result
from die import Die

die1 = Die()
die2 = Die()

results = [die1.roll() * die2.roll() for roll in range(1,1001)]

#for roll in range(1,1001):
#    result = die1.roll() * die2.roll()
#    results.append(result)

max_result = die1.num_sides * die2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

#for value in range(1, max_result + 1):
#    frequency = results.count(value)
#    frequencies.append(frequency)

x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_config = {'title' : 'Result', 'dtick' : 1}
y_config = {'title' : 'Frequency of result'}
layout = Layout(title="Frequencies of multiplying the results of rolling 2 dice 1000 times.", xaxis=x_config, yaxis=y_config)
offline.plot({'data' : data, 'layout' : layout}, filename='2xd6_multiply.html')