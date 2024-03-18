import pandas as pd
import numpy as np
import csv

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset
df1 = pd.read_csv('C:\\Users\\Ram\\Desktop\\Flight_project\\dataset.csv')
print(df1.columns)
# Define the column list for features (X) and the target variable (y)
column_list = ["Year", "Month", "DayofMonth", "DepTime","DepDelayMinutes", "OriginAirportID", "DestAirportID",
               "windspeedKmph", "winddirDegree", "precipMM", "visibility",
               "pressure", "DewPointF", "cloudcover", "WindGustKmph", "tempF", "WindChillF",
               "humidity", "time"]
X = df1[column_list]

y = np.where(df1["ArrDelayMinutes"] > 0, 1, 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create the Logistic Regression model
model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Evaluate the model on the test set
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Save the trained model to a binary file
filename = 'flight_model_logistic_regression.joblib'
joblib.dump(model, filename)
print(f"Model saved as {filename}")
'''
l = []

for index, row in df1.iterrows():
    if row["ArrDelayMinutes"] <= 30.0:
        l += [0]
        
    elif 4305 < row["ArrDelayMinutes"] <= 60.0:
        l += [1]
    
    else:
        l +=[2]
        
       
        
df1["delay_class"] = l

'''
y = df1['delay_class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_regression = LinearRegression()

# Train the model on the training data
linear_regression.fit(X_train, y_train)

# Make predictions on the test data
y_pred = linear_regression.predict(X_test)

# Calculate Mean Squared Error (MSE) and R-squared (R2) for evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

filename = 'linear_regression_model.bin'
joblib.dump(linear_regression, filename)
print(f"Model saved as {filename}")

