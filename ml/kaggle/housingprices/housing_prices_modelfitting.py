# Code you have previously used to load data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'somecitytrain.csv'

home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalePrice
# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Loop to find the ideal tree size from candidate_max_leaf_nodes

# non-pythonic approach
maes = {}
i = 0
for leaf_node in candidate_max_leaf_nodes:
    maes[i] = get_mae(leaf_node, train_X, val_X, train_y, val_y)
    i += 1

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
index = 0
min_mae = min(maes.values())
for key, value in maes.items():
    if value == min_mae:
        index = key        

best_tree_size = candidate_max_leaf_nodes[index]
print("Best Tree Size is", best_tree_size)

final_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=0)
final_model.fit(X, y)
print("Need sample data to predict... TODO")

