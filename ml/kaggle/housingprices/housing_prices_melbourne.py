# kaggle First Machine Learning Model
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
# print(melbourne_data.columns)

# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# target or y to be predicted
y = melbourne_data.Price # or melbourne_data["Price"]

# assume following features are enough to make a model and predict better
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# By convention, this data is called X
X = melbourne_data[melbourne_features]

# print(X.describe())
# print(X.head())

##########################
# without train/test split
##########################
# define model, specify a number for random_state to ensure same results each run
# melbourne_model = DecisionTreeRegressor(random_state = 1)

# fit the model
# melbourne_model.fit(X, y)

# print("Making predictions for the following 5 houses")
# print(X.head())
# predicted_home_prices = melbourne_model.predict(X)

# print("Actual prices are")
# print(y)
# print("Predicted prices are")
# print(predicted_home_prices)

# mae = mean_absolute_error(y, predicted_home_prices)
# print("Mean Absolute Error is ", mae) # it was around 1115.xx or so

##########################
# with train/test split
##########################
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state = 0)
melbourne_model = DecisionTreeRegressor(random_state = 1)
melbourne_model.fit(train_X, train_y)

test_predictions = melbourne_model.predict(test_X)
print("Mean Absolute Error is ", mean_absolute_error(test_y, test_predictions)) # seems to be around 273518.xxx