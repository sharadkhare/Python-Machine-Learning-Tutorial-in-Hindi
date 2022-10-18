# Polynomial Regression: if your data points clearly will not fit a linear regression(means straight line), than it might be ideal for a polynomial regression.
# it also uses relationship between the variables x and y to find the best way to draw a line through data point.
# how does it works: here we will register 18 cars as they were passing through certain toolbooth.
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
plt.scatter(x,y)
plt.show()

# now here we will import numpy and matplotlib and then we will draw the line of polynomial regression.
import numpy
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x,y, 3))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

# R -Squared: if there is no relationship between the x and y values than polynomial regression cannot predict anything. here the relationship is measured withthe value called R-squared
# R-Squared value ranges from 0 to 1, where 0 means no relationship and 1 means 100% related.
# python and the sklearn module will compute this value for you.
import numpy
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x,y, 3))
print(r2_score(y, mymodel(x)))


# for Predicting the future values.
# here we will predict the speed of a car passing at 17 PM
import numpy
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x,y, 3))
speed = mymodel(17)
print(speed)

# what balut the BAD fit? 
# lets create an example where polynimail regression woruld not be the best method to predict the future values.
import numpy
import matplotlib.pyplot as plt
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
mymodel = numpy.poly1d(numpy.polyfit(x,y, 3))
myline = numpy.linspace(2, 95, 100)
plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

# its R-Squared value?
import numpy
from sklearn.metrics import r2_score
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
mymodel = numpy.poly1d(numpy.polyfit(x,y, 3))
print(r2_score(y, mymodel(x)))