import pandas as pd
import numpy as np
import pandas_profiling

input_file = r'LondonA 1953 - 2012.csv'

col_type_dict = {
    'Date/Time': 'object',
     'Year': 'int64',
     'Month':'int64',
     'Day':'int64',
     'Time':'object',
     'Temp (°C)':'float64',
     'Temp Flag':'object',
     'Dew Point Temp (°C)':'float64',
     'Dew Point Temp Flag':'object',
     'Rel Hum (%)':'float64',
     'Rel Hum Flag':'object',
     'Wind Dir (10s deg)':'float64',
     'Wind Dir Flag':'object',
     'Wind Spd (km/h)':'float64',
     'Wind Spd Flag':'object',
     'Visibility (km)':'float64',
     'Visibility Flag':'object',
     'Stn Press (kPa)':'float64',
     'Stn Press Flag':'object',
     'Hmdx':'float64',
     'Hmdx Flag':'object',
     'Wind Chill':'float64',
     'Wind Chill Flag':'object',
     'Weather': 'object'
}


df = pd.read_csv(input_file,index_col=0,header=0, dtype = col_type_dict)

min_year = min(df['Year'])
max_year = max(df['Year'])

yearly_dict = {}
for year in np.arange(min_year,max_year+1):
    yearly_dict[year] = df[df['Year']==year]
    


