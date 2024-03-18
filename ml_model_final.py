import pandas as pd
import csv
import datetime as dt 
import requests
import joblib
import math

city_ID = {14747: 'SEA', 12478: 'JFK', 14107: 'PHX', 13204: 'MCO', 11292: 'DEN', 13303: 'MIA', 11298: 'DFW', 12266: 'IAH',
 12892: 'LAX', 12889: 'LAS', 14771: 'SFO', 13930: 'ORD', 10397: 'ATL', 11057: 'CLT', 11618: 'EWR'}




def predict_flight(year,month,day,origin, destination, dept_time,deptDelayMinutes,windspeedkmph,winddirDegree,precipMM,visibility,pressure,DewPointF,
                   cloudcover,WindGustKmph,tempF,WindChillF,humidity,time):
    

    for x in city_ID:
        if city_ID[x] == origin:
            origin_ID = x
        if city_ID[x] == destination:
            dest_ID = x

    # New data for prediction (DataFrame with the same columns as the training data)
    new_data = pd.DataFrame({
        'Year': [year],  # Replace 'value1', 'value2', and 'value3' with your new values
        'Month': [month],  # Replace 'value4', 'value5', and 'value6' with your new values
        'DayofMonth': [day] ,# Replace 'value7', 'value8', and 'value9' with your new values
        'DepTime':[dept_time],
        'DepDelayMinutes':[deptDelayMinutes],
        'OriginAirportID':[origin_ID],
        'DestAirportID':[dest_ID],
        'windspeedKmph':[windspeedkmph],
        'winddirDegree':[winddirDegree],
        'precipMM':[precipMM], 
        'visibility':[visibility], 
        'pressure':[pressure],
        'DewPointF':[DewPointF],
        'cloudcover':[cloudcover],
        'WindGustKmph':[WindGustKmph], 
        'tempF':[tempF], 
        'WindChillF':[WindChillF],
        'humidity':[humidity], 
        'time':[time],
    })

    filename = 'flight_model_logistic_regression.joblib'  # Replace with the filename you used for saving the model
    model1 = joblib.load(filename)
    # Make predictions on the new data
    predicted_outcomes = model1.predict(new_data)

    # Add the predicted outcomes to the new_data DataFrame (optional, for visualization purposes)
    # new_data['ArrDelayMinutes'] = predicted_outcomes

    if predicted_outcomes[0] == 0.0:
        return "Your flight will not be delayed :)"
    else:
        # return "Your flight is delayed. :("
        
        filename = 'linear_regression_model.bin'  # Replace with the filename you used for saving the model
        model2 = joblib.load(filename)
        # Make predictions on the new data
        predicted_outcomes1 = model2.predict(new_data)

        # Add the predicted outcomes to the new_data DataFrame (optional, for visualization purposes)
        # new_data['delay_class'] = predicted_outcomes1
        
        outcome = round(predicted_outcomes1[0])
        
        if outcome == 0:
            return "Your flight is delayed less than 30 minutes"
        elif outcome == 1:
            return "Your flight is delayed around 30-60 minutes"
        else :
            return "Your flight is by more than an hour"
     
