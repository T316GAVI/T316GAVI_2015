import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"


def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('�', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True, encoding='latin1')


weather_mar2012.columns = [s.replace('Â°', '') for s in weather_mar2012.columns]

weather_mar2012["Temp (C)"].plot(figsize=(15, 5))
plt.show()

weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')

print(weather_mar2012[:5])

weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)

print(weather_mar2012[:5])

temperatures = weather_mar2012[['Temp (C)']]
temperatures['Hour'] = weather_mar2012.index.hour

temperatures.groupby('Hour').aggregate(np.median).plot()
plt.show()

#data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

#weather_2012 = pd.concat(data_by_month)

#weather_2012.to_csv('weather_2012.csv')
