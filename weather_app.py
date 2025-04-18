import tkinter as tk
import requests

# Replace with your own OpenWeatherMap API key
API_KEY = "4aa50f67c5fc1bd647cf8665d6a7eb56"

def get_weather():
    city = city_entry.get()
    if city == "":
        result_label.config(text="Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text="City not found")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = f"📍 {city.title()}\n🌡️ Temp: {temp} °C\n🌤️ Condition: {condition.title()}\n💧 Humidity: {humidity}%\n🌬️ Wind: {wind} m/s"
        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="Error fetching data")

# --- GUI ---
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")
root.resizable(False, False)

# Input field
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Get Weather button
get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
get_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
