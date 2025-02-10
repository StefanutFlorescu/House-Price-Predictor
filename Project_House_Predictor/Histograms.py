#3. Looking/Visualizing at the data

import Model

import matplotlib.pyplot as plt
Model.housing.hist(bins=50, figsize=(20,15))
#Model.housing["ocean_proximity"].hist(bins=50, figsize=(20,15))
plt.show()