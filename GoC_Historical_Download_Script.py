import pandas as pd
import datetime
from dateutil import rrule
from datetime import datetime, timedelta


# Call Environment Canada API
# Returns a dataframe of data
def getHourlyData(stationID, year, month):
    base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    query_url = "format=csv&stationID={}&Year={}&Month={}&timeframe=1".format(stationID, year, month)
    api_endpoint = base_url + query_url
    return pd.read_csv(api_endpoint)

#stationID = 50093
stationID = input("Station ID: ")
start_date = input("Start Month (mmmYYYY): ")
#start_date = datetime.strptime('Mar2012', '%b%Y')
start_date = datetime.strptime(start_date, '%b%Y')
end_date = input("End Month (mmmYYYY): ")
#end_date = datetime.strptime('Apr2019', '%b%Y')
end_date = datetime.strptime(end_date, '%b%Y')

#make an empty list of all the dataframes
frames = []
#get each data frame for each month
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = getHourlyData(stationID, dt.year, dt.month)
    frames.append(df)

#combine monthly dataframes
weather_data = pd.concat(frames)

#format data frame
weather_data['Date/Time'] = pd.to_datetime(weather_data['Date/Time'])
weather_data['Temp (°C)'] = pd.to_numeric(weather_data['Temp (°C)'])

#save
weather_data.to_csv('station_%s_%s-%s.csv' % (stationID, start_date, end_date))
