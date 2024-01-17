# Linear Regression


import numpy as np
## Dependencies
from sklearn.linear_model import LinearRegression

## Data (Apple stock prices)
apple = np.array([155, 156, 157])
n = len(apple)

## One-liner
model = LinearRegression().fit(np.arange(n).reshape((n, 1)), apple)

## Result & puzzle
print(model.predict([[3], [4]]))
'''
[158. 159.]
'''
