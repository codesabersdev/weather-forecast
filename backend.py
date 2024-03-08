import requests
API_KEY = ""


def get_data(city, forecast_days, option):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    raw_data = response.json()
    filtered_data = raw_data["list"]
    nr_value = 8*forecast_days
    filtered_data = filtered_data[:nr_value]
    dates = [data["dt_txt"] for data in filtered_data]
    match option:
        case "Temperature":
            filtered_data = [float(data["main"]["temp"]) / 10 for data in filtered_data]
        case "Sky Conditions":
            filtered_data = [data["weather"][0]["main"] for data in filtered_data]

    return filtered_data, dates


if __name__ == "__main__":
    print(get_data(city="Sharjah", forecast_days=3, option="Temperature"))
