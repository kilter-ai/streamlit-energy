import os

import numpy as np
import pandas as pd


# daily_usage_df['Date'] = pd.to_datetime(daily_usage_df['Date'], format='%Y-%m-%d')
# daily_usage_df = daily_usage_df.set_index('Date')
# daily_usage_df['day_name']= daily_usage_df.index.day_name()
# # daily_usage_df.drop('Day',axis=1, inplace=True)

# daily_usage_df['dow'] = daily_usage_df.index.dayofweek
# daily_usage_df['doy'] = daily_usage_df.index.dayofyear
# daily_usage_df['year'] = daily_usage_df.index.year
# daily_usage_df['month'] = daily_usage_df.index.month
# daily_usage_df['quarter'] = daily_usage_df.index.quarter
# # daily_usage_df# df['weekday'] = df.index.weekday_name
# daily_usage_df['weekday'] = daily_usage_df.index.weekday
# # df['woy'] = df.index.weekofyear
# daily_usage_df['woy'] = daily_usage_df.index.isocalendar().week
# daily_usage_df['dom'] = daily_usage_df.index.day # Day of Month
# daily_usage_df['date'] = daily_usage_df.index.date

# Get URLs from environment variables
CSV_URLS = {
    "Usage": os.getenv("CSV_URL_1"),
    "Dataset 2": os.getenv("CSV_URL_2"),
    "Dataset 3": os.getenv("CSV_URL_3")
}
def real_data():
    pass

def simulate_power_data():
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="h")
    # Generate dates from Jan 1, 2023 to Mar 31, 2023, hourly
    df = pd.DataFrame({  # Simulating data for the power usage in KWh
        "timestamp": dates,
        "hour": dates.hour,
        # "day_of_week": dates.dayofweek,
        "is_weekend": dates.dayofweek >= 5,
        "is_working_day": dates.dayofweek != 6,
        "power_usage_kwh": np.random.normal(loc=0.2, scale=0.05, size=len(dates)),
        'dow': dates.dayofweek,
        'doy': dates.dayofyear,
        'year': dates.year,
        'month': dates.month,
        'quarter': dates.quarter,
        # # daily_usage_df# df['weekday'] = df.index.weekday_name
        # daily_usage_df['weekday'] = daily_usage_df.index.weekday
        # 'woy': dates.weekofyear,
         'woy': dates.isocalendar().week,
        'dom': dates.day  # Day of Month
        # daily_usage_df['date'] = daily_usage_df.index.date

    })
    df.to_csv("power_data.csv", index=False)  # Save the genrated data to a csv file


if __name__ == "__main__":
    simulate_power_data()