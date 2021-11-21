import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.ensemble import RandomForestClassifier

# Load training and test data
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Check how much % of women survived
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print("% of women who survived:", rate_women)

# Check how much % of men survived
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
print("% of men who survived:", rate_men)

# Intereted in Survived column values => this our target, to be predicted (y)
target = train_data["Survived"]

# Assume following features (x1, x2, x3, x4) are good enough
features = ["Pclass", "Sex", "SibSp", "Parch"]

# Convert non-categorical values to numerical values
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# Use RandomForest classifier
# model parameters
    # n_estimators = number of trees (tune this based on prediction accuracy)
    # max_depth = maximum depth of a tree (can be tuned as well)
    # random_state = something like a seed value... need to learn more on this
model = RandomForestClassifier(n_estimators=250, max_depth=7, random_state=1)
# find a model that fits
model.fit(X, target)
# predict for test data
predictions = model.predict(X_test)

# Prepare data frame based on test_data PassengerId and predicted value (Survived)
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
# Save the prediction to a csbv file
output.to_csv('shan_submission.csv', index=False)
