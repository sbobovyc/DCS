#! /bin/env python2.6

import numpy 
import matplotlib.pyplot as plt

#plt.figure()


x = numpy.arange(0, 5, 0.1);
y = numpy.sin(x)
plt.plot(x, y, 'r')

y = numpy.cos(x)
plt.plot(x, y, 'g')

y = numpy.tan(x)
plt.plot(x, y, 'b')

#create data
x_series = [0,1,2,3,4,5]
y_series_1 = [x**2 for x in x_series]
y_series_2 = [x**3 for x in x_series]
 
plt.plot(x_series, y_series_1, 'r-')



plt.show()
