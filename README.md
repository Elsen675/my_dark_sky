# Welcome to My Dark Sky ☁️
***

## Task
The problem was to create a robust, user-friendly weather application that provides real-time data, forecasts, and historical search tracking. The challenge lay in:
* Integrating multiple API endpoints (Current Weather & 5-Day Forecast).
* Implementing an efficient **caching mechanism** to stay within API rate limits and improve performance.
* Managing a persistent **SQLite database** to store and display recent search history.
* Deploying a full-stack Flask application to a production environment (Railway/Render).

## Description
I solved this problem by building a Flask-based web application with a modern, responsive UI. 
* **Backend:** Python with Flask for routing and logic.
* **Frontend:** HTML5 and **Tailwind CSS** with Glassmorphism design for a premium feel.
* **Data Persistence:** SQLAlchemy was used to track user searches in a local database.
* **Optimization:** A custom JSON-based caching system was built to store API responses for 5 minutes, significantly reducing external network calls.
* **API Integration:** Leveraged OpenWeatherMap's RESTful API for global weather data.

## Installation
To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-link]
    cd my_dark_sky
    ```

2.  **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    Create a `.env` file in the root directory and add your OpenWeather API Key:
    ```env
    OPENWEATHER_API_KEY=your_actual_api_key_here
    ```

## Usage
To start the development server:
bash
python app.py

Open your browser and navigate to http://10.8.2.76:5000/ (or localhost:5000).

Live Demo: My Dark Sky on Railway

Features
Real-time Weather: Accurate temperature, humidity, and wind speed.

5-Day Forecast: Daily breakdowns of upcoming weather conditions.

Search History: Sidebar tracking your most recent 5 searches.

Smart Caching: Fast loading times via local storage of recent requests.

Note: This project uses the OpenWeatherMap Free Tier. Historical "Time Machine" data is simulated or restricted based on current API plan limitations.

### The Core Team
Software Engineer: [Elshan]

Program: Full-Stack Software Engineering at Qwasar SV.

Made at Qwasar SV -- Software Engineering School

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
