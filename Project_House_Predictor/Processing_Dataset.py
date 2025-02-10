#5.
import Split_Data
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

housing_encoded = pd.get_dummies(Split_Data.housing, columns=["ocean_proximity"])

corr_matrix = housing_encoded.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))

# attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
# scatter_matrix(Split_Data.housing[attributes], figsize=(12, 8))
# plt.show()


# Split_Data.housing.plot(kind="scatter", x="median_income", y="median_house_value",
#     alpha=0.1)
# plt.show()

########## number of rooms per household and other useful information
housing = housing_encoded

housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]


corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))