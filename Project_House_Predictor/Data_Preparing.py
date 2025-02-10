#6.
import Split_Data

housing = Split_Data.strat_train_set.drop("median_house_value", axis=1)
housing_labels = Split_Data.strat_train_set["median_house_value"].copy()


############ Dealing with the column that is ambigous
housing.dropna(subset=["total_bedrooms"]) # Get rid of the corresponding districts  
housing.drop("total_bedrooms", axis=1) # Get rid of the whole attribute
median = housing["total_bedrooms"].median() # Set the values to some value (zero, the mean, the median, etc.)
housing["total_bedrooms"].fillna(median, inplace=True)


########## Solving the problem with a library

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")

housing_num = housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)

######### Those are the same
#print(imputer.statistics_)
#print(housing_num.median().values)

####### use this “trained” imputer to transform the training set by replacing
###### missing values by the learned medians
X = imputer.transform(housing_num)
