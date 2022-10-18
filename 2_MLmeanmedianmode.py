# Data Set: [99,86,87,88,111,86,103,87,94,78,77,85,86]
# in ML and in Mats also there are basically three values that are actually interest to us:
# Mean: the average value
# median: the mid point value
# Mode: the most common value.

# here in this example we have speed of 13 cars
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Mean: to calculate the mean , sum all the values 
# sum of all speed/cars (99+86+87+88+111+86+103+8794+78+77+85+86)/13
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
sharad = numpy.mean(speed)
print(sharad) # 89.77 is its avg speed

# Median: here we will find the middle value
import numpy as np
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
sharad = np.median(speed)
print(sharad)

# speed = [2,4,6,8,10,12] 6+8/2=7

# mode: the value that appears most number of times: we will use scipy mode()
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
sharad = stats.mode(speed)
print(sharad)

