# Regression: The term regression is used when you try to find out the relationship between the variables.in machine learning and in statical modeling that relatioship is used to predict the outcome of the future event.
# Linear Regression: it basically uses the relationship between the data points to draw a straight line through all of them., this line can be used to predict the future.

# How does it works:
# now we will start by drawing a scatter plot.
# x is the age of 13 cars and y is the tollbooth where the cars passes.
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

# now we will import scipy(scintific python) and draw te line of linear regression.
import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept 
mymodel = list(map(myfunc, x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

# Lines to make our compliler able to draw:
'''plt.savefig(sys.stdout.buffer)
sys.stdout.flush()'''

# Defining R for Relationship - it is important to know how the relationship between the values x axis and y axis, if there is no relationship then the linear regression cannot be used to prediect anything. than this relationship is called R and alos known as the coefficient of corelation.

# the R values vanges from -1 to 1, where 0 means no relationship and 1 and -1 means 100% realted.

# now we will know how well does the data fit in a linear regression:
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
slope, intercept, r, p ,std_err = stats.linregress(x,y)
print(r)

# predict fucture values: lets try to predict the speed of 10 years old car.
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85,86]
slope, intercept,r , p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)
print(speed)

# Bad Fit - lets create an ex: where linear regression would not be the best ethod for predicting the future:
import matplotlib.pyplot as plt
from scipy import stats
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,36,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p ,std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

# now we will check the relationship with R
import numpy
from scipy import stats
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,36,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept, r, p ,std_err = stats.linregress(x,y)
print(r)
