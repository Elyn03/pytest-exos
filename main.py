import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

import matplotlib.pyplot as plt
import numpy as np

import json

def fetch_weather_data(latitude: float, longitude: float, variable: str = "temperature_2m") -> pd.DataFrame:
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": variable
    }
    responses = openmeteo.weather_api(url, params = params)
    response = responses[0]

    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()}{response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    values = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        ),
        variable: values
    }

    hourly_data[variable] = values
    return pd.DataFrame(data = hourly_data)


def save_to_json(df: pd.DataFrame, filename: str) -> None:
    df_copy = df.copy()
    df_copy['date'] = df_copy['date'].astype(str)
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(df_copy.to_dict(orient='records'), f, indent=4)


def plot_temperature(df: pd.DataFrame, variable: str = "temperature_2m"):
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df[variable], label=variable, color="blue")
    plt.title("Évolution de la température")
    plt.ylabel("Température (°C)")
    plt.grid(True)
    plt.legend()
    plt.show()


# df = fetch_weather_data(48.85, 2.35)  # Paris, par exemple
# plot_temperature(df)