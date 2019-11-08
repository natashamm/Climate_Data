
import pandas as pd
from dateutil import rrule
from datetime import datetime
import weatherdata.helpers.weather_api as weather_api

# edmonton south campus
#stationID = 53718
# UofA
stationID = 1801
# !!! To Do: get closest station by address
#address = input("Address:")
#latlon = geographic.getLatLon(address)
#stationID = geographic.getStationID(latlon[0], latlon[1])

# stationID = input("Station ID: ")
start_date = input("Start Month (mmmYYYY): ")
# start_date = datetime.strptime('Mar2012', '%b%Y')
start_date = datetime.strptime(start_date, '%b%Y')
end_date = input("End Month (mmmYYYY): ")
# end_date = datetime.strptime('Apr2019', '%b%Y')
end_date = datetime.strptime(end_date, '%b%Y')

# make an empty list of all the dataframes
frames = []
# get each data frame for each month
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = weather_api.getDailyData(stationID, dt.year, dt.month)
    frames.append(df)

# combine monthly dataframes
weather_data = pd.concat(frames)

# format data frame
#weather_data['Date/Time'] = pd.to_datetime(weather_data['Date/Time'])
#weather_data['Temp (°C)'] = pd.to_numeric(weather_data['Temp (°C)'])

# take only relevant variables
# weather_data = weather_data[['Date/Time', 'Temp (°C)',
#							 'Dew Point Temp (°C)', 'Rel Hum (%)']]
# rename columns
# weather_data = weather_data.rename(columns={"Temp (°C)": "Temp (degrees celsius)",
#										    "Dew Point Temp (°C)": "Dew Point Temp (degrees celsius)"})

# save
weather_data.to_csv('/Users/Natasha/Desktop/Climate_Data/downloads/station_%s_%s-%s.csv' % (stationID, start_date, end_date), index=False)


