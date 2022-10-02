# Using City Name

from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

@app.route('/temperature',methods=['POST'])
def temperature():
    city = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=01d1f6ccaffe5c8f36a6196d7c7485a6')

    json_object = r.json()
    
    weather = json_object['weather'][0]['main']
    temp_k = float(json_object['main']['temp'])
    temp_c = int(temp_k-273.15)
    
    return render_template('temperature.html', temp=temp_c, weather=weather, city=city.capitalize())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#Using ZipCode
@app.route('/temperature_fahrenheit', methods=['POST'])
def temperature_celsius():
   zipcode = request.form['zip']
   r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=01d1f6ccaffe5c8f36a6196d7c7485a6')
   
   json_object = r.json()
   
   weather = json_object['weather'][0]['main']
   temp_k = float(json_object['main']['temp'])
   temp_f = (temp_k - 273.15) * 1.8 + 32
   
   return render_template('temperature.html', temp=temp_f, weather=weather, city=city.capitalize())


