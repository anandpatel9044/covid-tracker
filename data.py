import requests
import pandas as pd

def get_global_data():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    res = requests.get(url)
    data = res.json()

    df = pd.DataFrame({
        "date": data["cases"].keys(),
        "cases": data["cases"].values(),
        "deaths": data["deaths"].values(),
        "recovered": data["recovered"].values()
    })

    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%y")

    # Daily cases
    df["daily_cases"] = df["cases"].diff()

    # 7-day avg
    df["7_day_avg"] = df["daily_cases"].rolling(7).mean()

    return df


def get_country_data():
    url = "https://disease.sh/v3/covid-19/countries"
    res = requests.get(url)
    data = res.json()

    df = pd.DataFrame(data)

    return df[["country", "countryInfo", "cases", "deaths", "recovered", "tests"]]