import random
import matplotlib.pyplot as plot
import numpy as np


# set up your lists

numlist = [10, 10, 2, 4]
namelist = ['female', 'male', 'hermaphrodite', 'asexual']
colorlist = ['blue', 'red', 'purple', 'green']
explodelist = [0.0, 0.0, 0.2, 0.0]

# make the pie chart

plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
         explode=explodelist, startangle=75)
plot.axis('equal')
plot.savefig('piechart.png')
