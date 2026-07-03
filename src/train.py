from utils import *
from preprocess import *


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state= 2)


# *** RANDOM FOREST REGRESSOR ***

regressor = RandomForestRegressor(n_estimators =100)
# training th model
regressor.fit(X_train, Y_train)
