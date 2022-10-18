# Grid Search: one method is to try out different values and then picj the value that gives the best score. this technique is known as grid search.
'''
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris['data']
y = iris['target']
logit = LogisticRegression(max_iter=10000)
print(logit.fit(x,y))
print(logit.score(x,y))
'''
# now here we will implement Grid Search
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris['data']
y = iris['target']
logit = LogisticRegression(max_iter=10000)
C = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]
scores= []
for choice in C:
    logit.set_params(C=choice)
    logit.fit(x,y)
    scores.append(logit.score(x,y))
print(scores)    

# what about best practices
# refer to the chapter train/test in scipy and in ML.