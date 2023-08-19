import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

#function to get temperature
def get_temperature(data, timestamp):
    for entry in data['list']:
        if entry['dt_txt'] == timestamp:
            result = entry['main']['temp']
            result -= 273.15
            result = round(result, 2)
            return result
    return None

#function to get wind speed
def get_wind_speed(data, timestamp):
    for entry in data['list']:
        if entry['dt_txt'] == timestamp:
            return entry['wind']['speed']
    return None

#function to get pressure
def get_pressure(data, timestamp):
    for entry in data['list']:
        if entry['dt_txt'] == timestamp:
            return entry['main']['pressure']
    return None

#main function
def main():
    response = requests.get(API_URL)
    data = response.json()

    while True:
        print("\n1. Get Temperature\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice in ['1', '2', '3']:
            timestamp = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            if choice == '1':
                temperature = get_temperature(data, timestamp)
                if temperature is not None:
                    print(f"Temperature at {timestamp}: {temperature} °C")
                else:
                    print("Data not found for the given timestamp.")
            elif choice == '2':
                wind_speed = get_wind_speed(data, timestamp)
                if wind_speed is not None:
                    print(f"Wind Speed at {timestamp}: {wind_speed} m/s")
                else:
                    print("Data not found for the given timestamp.")
            elif choice == '3':
                pressure = get_pressure(data, timestamp)
                if pressure is not None:
                    print(f"Pressure at {timestamp}: {pressure} hPa")
                else:
                    print("Data not found for the given timestamp.")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
