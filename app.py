from flask import Flask, render_template, request, session
from datetime import date,time
from API import get_weather
import ml_model_final
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# Variables to store the user input data
# selected_date = None
# departure_time = None
# origin_city = None
# destination_city = None
# year = None
# month = None
# day = None
# weather_data = None  # Variable to store weather data
# dep_delay = None

@app.route('/', methods=['GET', 'POST'])
def index():
    # global selected_date, departure_time, origin_city, destination_city, year, month, day, dep_delay
    current_date = str(date.today())
    if 'csrf_token' not in session:
        # Generate a unique CSRF token for the session
        session['csrf_token'] = secrets.token_hex(16)
    
    if request.method == 'POST'and request.form.get('csrf_token') == session['csrf_token']:
        departure_time = request.form['departure_time']
        origin_city = request.form['origin']
        destination_city = request.form['destination']
        dep_delay = request.form['departure_delay']
        # Extract year, month, and day separately
        year, month, day = map(int, current_date.split('-'))
        
        weather_data = get_weather(origin_city)

    # Display the weather data in app.py itself
        i = int(departure_time[:2])
        mini_info = weather_data['forecast']['forecastday'][0]['hour'][i]

        windspeedkmph = mini_info['wind_kph']
        winddirDegree = mini_info['wind_degree']
        precipMM = mini_info['precip_mm']
        visibility = mini_info['vis_km']
        pressure = mini_info['pressure_mb']
        DewPointF =  mini_info['dewpoint_f']
        cloudcover = mini_info['cloud']
        WindGustKmph = mini_info['gust_kph']
        tempF = mini_info['temp_f']
        WindChillF = mini_info['windchill_f']
        humidity = mini_info['humidity']
        time = str(i)+'00'
        
        dept_time = float(departure_time[:2]+departure_time[3:])
        
        result = ml_model_final.predict_flight(year,month,day,origin_city, destination_city, dept_time,dep_delay,windspeedkmph,winddirDegree,precipMM,visibility,pressure,DewPointF,
                   cloudcover,WindGustKmph,tempF,WindChillF,humidity,time)
        
        session['csrf_token'] = secrets.token_hex(16)
        
        return render_template('index.html', current_date=current_date, result=result, csrf_token=session['csrf_token'])
        
    else:
        return render_template('index.html', current_date=current_date, result=None, csrf_token=session['csrf_token'])

    


     

if __name__ == '__main__':
    app.run(debug=True)
