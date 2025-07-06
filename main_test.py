import pandas as pd
from main import fetch_weather_data

def test_fetch_weather_data():
    df = fetch_weather_data(48.85, 2.35)
    assert isinstance(df, pd.DataFrame)
    assert "temperature_2m" in df.columns
    assert len(df) > 0

def test_data_time_format():
    df = fetch_weather_data(48.85, 2.35)
    assert pd.api.types.is_datetime64_any_dtype(df["date"])


if __name__ == "__main__":
    test_fetch_weather_data()
    test_data_time_format()
