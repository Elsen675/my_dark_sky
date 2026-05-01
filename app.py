import os
import time
import json
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from models import db, WeatherSearch

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

with app.app_context():
    db.create_all()

def get_weather(city):
    cache_dir = '/tmp/cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    cache_path = f"{cache_dir}/{city.lower()}.json"
    current_time = time.time()

    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            cache_data = json.load(f)
            if current_time - cache_data['timestamp'] < 300:
                print(f"--- {city} melumat KESDEN geldi ---")
                return cache_data['data']
    
    print(f"--- {city} ucun API-a sorgu atildi ---")
    if not API_KEY:
        print("DIQQET: API_KEY tapilmadi! Vercel Environment Variables hissesini yoxlayin.")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_path, 'w') as f:
                json.dump({'timestamp': current_time, 'data': data}, f)
            return data
        return None
    except Exception as e:
        print(f"DEBUG: Sorgu zamani gozlenilmez xeta: {e}")
        return None

def get_forecast(city):
    cache_dir = '/tmp/cache'
    cache_path = f"{cache_dir}/{city.lower()}_forecast.json"
    current_time = time.time()

    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            cache_data = json.load(f)
            if current_time - cache_data['timestamp'] < 300:
                return cache_data['data']

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
            with open(cache_path, 'w') as f:
                json.dump({'timestamp': current_time, 'data': data}, f)
            return data
    except:
        return None
    return None

@app.route('/')
def index():
    city = request.args.get('city', 'Baku')
    weather_data = get_weather(city)
    forecast_data = get_forecast(city)

    if weather_data:
        try:
            new_search = WeatherSearch(
                city=weather_data['name'],
                temp=weather_data['main']['temp'],
                description=weather_data['weather'][0]['description']
            )
            db.session.add(new_search)
            db.session.commit()
        except Exception as e:
            print(f"Baza xetasi: {e}")
            db.session.rollback()
        
    history = WeatherSearch.query.order_by(WeatherSearch.timestamp.desc()).limit(5).all()
    return render_template('index.html', weather=weather_data, forecast=forecast_data, history=history)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)