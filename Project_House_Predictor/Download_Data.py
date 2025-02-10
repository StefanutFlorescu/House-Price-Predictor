#1. The first thing, we need to download the data

import os
import tarfile
import urllib.request

# Define constants
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

# Function to fetch housing data
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):  # Check if the directory exists
        os.makedirs(housing_path)  # Create the directory if it does not exist
    tgz_path = os.path.join(housing_path, "housing.tgz")
    
    # Download the file from the URL
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    # Extract the tar file
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

# Call the function to fetch the data
fetch_housing_data()
