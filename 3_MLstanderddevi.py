# standard Deviation: how the values are spread
speed = [86,87,88,86,87,85,86]
# there are 2 types of SD: Low SD and High SD.

# ex: for Low SD:
import numpy
speed = [86,87,88,86,87,85,86]
sharad = numpy.std(speed)
print(sharad)

# Ex: for High SD:
import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
sharad = numpy.std(speed)
print(sharad)

# Variance: how the values are spread
# if you take the squre root of the variance you will get the SD.
# to calculate the variance you have to do the below thing:
# (32 + 111 + 138 + 28 + 59 + 77 + 97)/7 = 77.4
# 32 - 77.4 =   -45.6 -> square root -> 2079.16
# 111-77.4=     33.5 ----- 1122.25
# 138-77.4=     61.6 ------ 3794.56
# 28-77.4=      -49.4 ------ 2440.36
# 59-77.4=      -18.4 ----- 338.56
# 77-77.4 =     -0.5 ----- 0.25
# 97-77.4 =     19.6 ----- 384.16

# the variace is the average number of these squared difference:

# (2079.16 + 1122.25+3794.56 + 2440.36 + 338.56 + 0.25 + 384.16)/7 = 1451.05

# As we learned the formula to find the SD is the square root of the vaiance.
# Squareroot of 1451.05 = 37.84

# Example of numpy std() 
import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
sharad = numpy.std(speed)
print(sharad)

# Symbol of SD and Variance:
# Standard Deviation Symbol = σ
# Variance Symbol = σ2