# In machine learning we create a models to predict the outcome, to measure of the model is good enough or need to rectify, than we use a method called train/test.
# what is train/test: 80% for training and 20% for testing.
# understanding with a proper data set:
# here for understanding we will use a data set that show 100 customers in a shop and their shopping habbits.
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
sharad1 = numpy.random.normal(3, 1, 100)
sharad2 = numpy.random.normal(150, 40, 100)/sharad1

plt.scatter(sharad1, sharad2)
plt.show()

# result: x axis represent the number of minutes before making the purchase and y axis represent the amount of the money spent on the purchase.

# next is splitting into train/test
# train_x = x[:80]
# train_y = y[:80]
# test_x = x[80:]
# test_y = y[80:]

# how to disply the training set:

# plt.scatter(train_x, train_y)
# plt.show()

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
plt.scatter(train_x, train_y)
plt.show()

# now we will display the testing set:
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
plt.scatter(test_x, test_y)
plt.show()

# what about fit the data set.
# here we will draw a polynomial regression line through the data point.
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6 ,100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# here we will use R-Squared r2.
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))
print(r2)

# now we will bring this to the testing set.
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

# now we will predict the values:
# in the below example we will see how much money will a customer spent if he or she in the shop stay for 5 min.
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100)/x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
print(mymodel(5))