import tkinter as tk
import requests

def get_weather():
    api_key = 'c8443219af7bede71b090f5d398916d6'
    city_name = city_entry.get()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature_label.config(text="Temperature: {:.1f}°C".format(data['main']['temp']))
        weather_label.config(text="Weather: " + data['weather'][0]["description"])
        humidity_label.config(text="Humidity: {}%".format(data['main']['humidity']))
        wind_speed_label.config(text="Wind Speed: {:.2f} m/s".format(data['wind']['speed']))
    else:
        temperature_label.config(text="Enter the city name correctly")
        weather_label.config(text="")
        humidity_label.config(text="")
        wind_speed_label.config(text="")

# Create tkinter window
window = tk.Tk()
window.title("Weather App")

# City input
city_label = tk.Label(window, text="Enter city:")
city_label.grid(row=0, column=0)
city_entry = tk.Entry(window)
city_entry.grid(row=0, column=1)

# Button to fetch weather
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.grid(row=0, column=2)

# Labels to display weather information
temperature_label = tk.Label(window, text="")
temperature_label.grid(row=1, columnspan=3)

weather_label = tk.Label(window, text="")
weather_label.grid(row=2, columnspan=3)

humidity_label = tk.Label(window, text="")
humidity_label.grid(row=3, columnspan=3)

wind_speed_label = tk.Label(window, text="")
wind_speed_label.grid(row=4, columnspan=3)

window.mainloop()
