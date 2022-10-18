# Scatter Plot: A scatter plot is a diagram where each value in the data set represented by the Dots.
# it basically needs 2 array of the same length one for x axis and another for y axis.
# in the below example x array represents the age of each car and the y array represet the speed of each car.
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

# Now we will do the above via random data dist.
# lets create 2 array that are both filled with 1000 random numbers from normal data dist, the 1st array will have the mean set 5.0 with standard deviation of 1.0. the 2nd array will have the mean set to 10.0 with the standard deviation of 2.0.

import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x,y)
plt.show()