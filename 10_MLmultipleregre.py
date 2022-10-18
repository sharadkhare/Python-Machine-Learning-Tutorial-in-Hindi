# Multiple regression: it like the linear regression but with more than one independent value, meaning that we try to predict a value based on two or more variables:

# How does the whole process work:
# for this we will start from importing the Pandas Module
# df = pandas.read_csv("cars.csv")
# then after this we will make a list of independent values and call this variable x, put the dependent value in a variable called y.
# x = df[['Weight', 'Volume']]
# y = df['CO2']
# now we will use some methods from sklearn module, so we will have to import that module as well.
# from sklearn import linear_model
# from sklearn module we will use the LinearRegression() method to create a linear regression object.
# this objects has a method called fit() that takes the independent and dependent values as a parameters and fills the regression objects with the data that descibes the relationship.
# regr = linear_model.LinearRegression()
# regr.fit(x,y)

# now here we will predict the CO2 of a car where the weight is 2300kg and the volume is 1300
# predictedCO2 = regr.predict([[2300, 1300]])

# example in action after theory:
import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(x,y)
# now here we will predict the CO2 of a car where the weight is 2300kg and the volume is 1300
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)

# Coefficient: this is a factor that describes the relationship with an unkwon variable.
# example: if x is a variable then 2x is x two times. x is unkown varible and number 2 is the coefficient.

# here we will print the coefficient values of the regression object

import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(x,y)
print(regr.coef_)

# explaing the output above: 
# [0.00755095 0.00780526] weight and volume.
# these values tell us that if the weight increase by 1 kg then the CO2 emission increases by 0.00755095 and if the volume increases by 1, then the CO2 emission increases by 0.00780526.

# what if i will increase the weight with 1000 kg
import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(x,y)
# now here we will predict the CO2 of a car where the weight is 2300kg and the volume is 1300
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)

# for the calculation here we will show that the coefficient of 0.00755095 is correct.and the answer will be below:
# 107.2087328 + (1000*0.00755095) = 114.75968007