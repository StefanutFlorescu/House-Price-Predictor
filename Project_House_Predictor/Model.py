#2. Processing the Data

import os
import pandas as pd
import Download_Data

# Loads the data
def load_housing_data(housing_path=Download_Data.HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# Printing the Data
housing = load_housing_data()

########## Get INFORMATION about the data (technical)
#print(housing.info())

########## Get DESCRIPTION about the data (stats)
#print(housing.describe())

######### See the first 5 elements of the data
#print(housing.head())

######### You can print exactly which columns you want by the name + count the different types
#print(housing["ocean_proximity"])
#print(housing["ocean_proximity"].value_counts())