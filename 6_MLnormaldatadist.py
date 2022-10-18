# Normal Data Dist: In numpy probability theory this kind of data dist is known as normal data dist or Gaussian Data Dist, where the values are concentrated around a given value.
# a Example of normal data dist:
import numpy
import matplotlib.pyplot as plt
sharad = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(sharad, 100)
plt.show()
# a normal data dist is also known as bell curve because of it's bell shape.