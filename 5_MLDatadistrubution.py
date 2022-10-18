# Data Distribution: How do we get te big data set?
# here now we will create a array containing 250 random floats between 0.0 to 5.0
import numpy as np
sharad = np.random.uniform(0.0, 5.0, 250)
print(sharad)

# to visualize the big data set we can draw a histogram with the data we got:
# here we will use python module matplotlib.
import numpy as np
import matplotlib.pyplot as plt
sharad = np.random.uniform(0.0, 5.0, 250)
plt.hist(sharad, 5)
plt.show()

# Big Data Distribution 
# now we will create an array with 100000 random numbers and display them using the hist with 100 bars.
import numpy as np
import matplotlib.pyplot as plt
sharad = np.random.uniform(0.0, 5.0, 100000)
plt.hist(sharad, 100)
plt.show()