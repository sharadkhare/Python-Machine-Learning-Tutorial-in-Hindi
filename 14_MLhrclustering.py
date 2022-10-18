# hierarchical Clustering: it is an unsupervised learning method for clustering data points. the algorithm builds clusters by measuring the dissimilarities between the data.
#example for the same:
# three lines to make our compiler able to draw.
import numpy as np
import matplotlib.pyplot as plt

x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
plt.scatter(x,y)
plt.show()

# now we will compute the ward linkage method using euclidean distance and visualize it using the dendogram.
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
data = list(zip(x,y))
linkage_data= linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)
plt.show()

# yes, we can do the same thing with the python scikit-learn , and visualize on a 2-D plot.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]
data = list(zip(x,y)) # turn the data into a set of points
hierarchical_cluster = AgglomerativeClustering(n_clusters=2,affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data) # this fit_predict method can be called on the data to compute the cluster using te defined paramenter.
plt.scatter(x,y, c=labels)
plt.show()