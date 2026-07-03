from cProfile import label
from utils import *
from preprocess import *
from train import *

# *** EVALUATION ***
test_data_prediction = regressor.predict(X_test)
print(test_data_prediction)

# R Squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error: ", error_score)

# *** Compare the actual values and predicted values in a plot

Y_test = list(Y_test)

plt.plot(Y_test, color = 'blue', label = 'Actual Value')
plt.plot(test_data_prediction, color = 'green', label = 'Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show

# Prediction
input_data = pd.DataFrame(
    [[1447.160034, 78.470001, 15.18, 1.471692]],
    columns=['SPX', 'USO', 'SLV', 'EUR/USD']
)

prediction = regressor.predict(input_data)

print("Predicted Gold Price:", prediction[0])
