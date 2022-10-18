# Categorical Data: instead of igoring the categorical data and excluding the information from our model, you can transfrom the data so that it can be used to our models.
'''
import pandas as pd
cars = pd.read_csv('cars.csv')
print(cars.to_string())'''


# example of one hot encoding
import pandas as pd
cars = pd.read_csv('cars.csv')
ohe_cars = pd.get_dummies(cars[['Car']])
print(ohe_cars.to_string())

'''
# now we will predit c02 on the basis of above:
import pandas as pd
from sklearn import linear_model

cars = pd.read_csv('cars.csv')
ohe_cars = pd.get_dummies(cars[['Car']])
x = pd.concat([cars[['Volume', 'Weight']], ohe_cars, axis=1])
y = cars['CO2']
regr= linear_model.LinearRegression()
regr.fit(x,y)
# for predicting the CO2 emmision of a volvo where the weight is 2300 and the volume is 1300.
regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])'''