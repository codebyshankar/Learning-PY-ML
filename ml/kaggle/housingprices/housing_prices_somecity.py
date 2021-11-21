# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

# what columns are there and decide on y
# home_data.columns # SalePrice is what we need
y = home_data["SalePrice"]

# Create the list of features below
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Review data
# print description or statistics from X
# print(X.describe())
# print(X.head())

#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state = 1)

# Fit the model
iowa_model.fit(X, y)

# for now, predict using same trained data
predictions = iowa_model.predict(X)
print(predictions)

# compare actual with prediction (simple and poor print stmts)
print("actual price y:\n", y.head())
print("predicted price\n:", predictions)