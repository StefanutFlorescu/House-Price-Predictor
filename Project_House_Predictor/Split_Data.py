#4. Split the Data into Train and Tests 

import Model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from zlib import crc32
import matplotlib.pyplot as plt

############# Splitting the data Randomly
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

########### Splitting the data after Giving it a unique identifier
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32
def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing_with_id = Model.housing.reset_index() # adds an `index` column

# train_set, test_set = split_train_test(Model.housing, 0.2)
#train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")


########### Using a predefined library that separates the data
train_set, test_set = train_test_split(Model.housing, test_size=0.2, random_state=42)


######## Using a predefined library to get the PERCHANTAGE of people exactly of how much money the make
Model.housing["income_cat"] = pd.cut(Model.housing["median_income"],
    bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
    labels=[1, 2, 3, 4, 5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(Model.housing, Model.housing["income_cat"]):
    strat_train_set = Model.housing.loc[train_index]
    strat_test_set = Model.housing.loc[test_index]

###### Data is back to its original state
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
 
# print(len(train_set))
# print(len(test_set))

housing = strat_train_set.copy()

####### Making a map of those houses
#housing.plot(kind="scatter", x="longitude", y="latitude")
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
 s=housing["population"]/100, label="population", figsize=(10,7),
 c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
)
# plt.legend()
# plt.show()



