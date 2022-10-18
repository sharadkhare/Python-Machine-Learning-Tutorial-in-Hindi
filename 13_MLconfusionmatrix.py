# what is Confusion Matrix? - it is a table that is used in classification problems to assess where errors in the model where made. here the rows represent the actual classes the outcome should have been. whlie the columns represent the prediction.
# now we will create a confution matrix:

import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix= confusion_matrix, display_labels=[False, True])
cm_display.plot()
plt.show()

# True means the values are accurately predicted, false means there was an error or wrongly predicted.

# Created Metrics:
# Accuracy: it measures how often the model is correct.
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
accuracy = metrics.accuracy_score(actual, predicted)
print(accuracy)

# Precision: of the positive predicted, what is the percentage of truly positive?
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
precision = metrics.precision_score(actual, predicted)
print(precision)

# Sensitivity (Recall): of all the positive cases, what is the percentage of positive prediction?
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
sensrecall = metrics.recall_score(actual, predicted)
print(sensrecall)

# Specificity: How well the model is at predicting the negative result?
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
specify = metrics.recall_score(actual, predicted, pos_label=0)
print(specify)

# F-Score: it is the harmonic mean of the precision and sensitivity: it consider both false positive and false negative cases.
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
f1score = metrics.f1_score(actual, predicted)
print(f1score)

# How to use all of them is a single code:
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)
accuracy = metrics.accuracy_score(actual, predicted)
precision = metrics.precision_score(actual, predicted)
sensrecall = metrics.recall_score(actual, predicted)
specify = metrics.recall_score(actual, predicted, pos_label=0)
f1score = metrics.f1_score(actual, predicted)
print({"Accuracy":accuracy, "Precision":precision, "Sensitivity_recall":sensrecall, "Specificity":specify, "F1_score":f1score})