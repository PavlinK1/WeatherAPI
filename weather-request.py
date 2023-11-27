import requests
import sqlite3
import json
import math

# Map icon with weather code
def get_weather_icon(code):
    if 200 <= code <= 233:
        return "⛈️"
    elif 300 <= code <= 302:
        return "🌦️"
    elif 500 <= code <= 522:
        return "🌧️"
    elif 601 <= code <= 623:
        return "🌨️"
    elif 700 <= code <= 707:
        return "🌫️"
    elif 801 <= code <= 803:
        return "⛅"
    elif code == 804:
        return "☁️"
    elif code == 800:
        return "☀️"
    else:
        return "❓"


def colorize_weather_description(code, desc):
    colors = {
    "YELLOW":"\033[0;33m",
    "LIGHT_BLUE":"\033[0;34m"
    }

    if code == 800:
        return f"{colors['YELLOW']} {desc}"
    else:
        return f"{colors['LIGHT_BLUE']} {desc}"


def dump_json_file(data):
    # Only for testing purposes
    with open('weather_data.log', 'w') as json_file:
        json.dump(data, json_file, indent=4)


def fetch_and_push_weather_data(api_key, city, conn):
    try:
        # Fetch API data
        response = requests.get(f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}")
        data = response.json()

        if "status_message" in data:
            print(f"Error: {data['status_message']}")
            return

        if "data" not in data:
            print(f"Error: Unable to retrieve weather data for {city}. Check the city name and try again.")
            return

        # Extract required data
        temperature = math.floor(data['data'][0]['temp'])
        description = data['data'][0]['weather']['description']
        icon_code = data['data'][0]['weather']['code']
        timestamp = data['data'][0]['ob_time']

        dump_json_file(data) # Dump json file
        colored_description = colorize_weather_description(icon_code, description) # Colorize weather description
        icon = get_weather_icon(icon_code) # Map icon

        print(f"{city}", end="  ")
        print(f"{icon}", end="  ")
        print(f"{temperature}°C", end="  ")
        print(f"{colored_description}")

        # Push API data to an existing database
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?)",
                           (city, temperature, description, timestamp))
            conn.commit()

    except requests.exceptions.RequestException as e:
        print(f"Error: An HTTP request error occurred - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    city = input("Enter the city for weather data (e.g., Sofia): ")
    db_file = 'weather_data.db'
    api_key = 'bbae9873664845138b207d66af7d2c72'  # Weatherbit API key
    conn = sqlite3.connect(db_file)
    fetch_and_push_weather_data(api_key, city, conn)
    if conn: conn.close()


if __name__ == "__main__":
    main()
