import requests
import matplotlib.pyplot as plt
import datetime

# OpenWeatherMap API Key (Replace 'YOUR_API_KEY' with a valid key)
API_KEY = "f80bf882726bd788cec20db36026b7b6"
CITY = "Chennai"  # Change to any city
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    """Fetch weather forecast data from OpenWeatherMap API."""
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

def process_weather_data(data):
    """Extract relevant data for visualization."""
    dates, temps, humidity, wind_speed = [], [], [], []
    
    for entry in data["list"]:
        dt = datetime.datetime.fromtimestamp(entry["dt"])
        dates.append(dt)
        temps.append(entry["main"]["temp"])
        humidity.append(entry["main"]["humidity"])
        wind_speed.append(entry["wind"]["speed"])
    
    return dates, temps, humidity, wind_speed

def plot_weather(dates, temps, humidity, wind_speed):
    """Create a visualization dashboard with Matplotlib."""
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.set_xlabel("Date & Time")
    ax1.set_ylabel("Temperature (°C)", color="tab:red")
    ax1.plot(dates, temps, color="tab:red", label="Temperature")
    ax1.tick_params(axis="y", labelcolor="tab:red")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Humidity (%) & Wind Speed (m/s)", color="tab:blue")
    ax2.plot(dates, humidity, color="tab:blue", linestyle="--", label="Humidity")
    ax2.plot(dates, wind_speed, color="tab:green", linestyle="--", label="Wind Speed")
    ax2.tick_params(axis="y", labelcolor="tab:blue")

    fig.autofmt_xdate()
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    
    plt.title(f"Weather Forecast for {CITY}")
    plt.show()

# Fetch and visualize weather data
weather_data = fetch_weather_data()
if weather_data:
    dates, temps, humidity, wind_speed = process_weather_data(weather_data)
    plot_weather(dates, temps, humidity, wind_speed)