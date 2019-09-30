import pandas as pd
import datetime
from dateutil import rrule
from datetime import datetime, timedelta
import climatedata.helpers.get_distance


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
