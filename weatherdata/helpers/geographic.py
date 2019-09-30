import pandas as pd
import geopy.geocoders


#for a given lat lon, return the station id of the closest station
def getStationID(lat, lon):
	stations = pd.read_csv('/Users/Natasha/Desktop/Climate_Data/Station Inventory EN.csv', skiprows=3)
	#stations['Latitude (Decimal Degrees)']
	#stations['Longitude (Decimal Degrees)']
	stations['Distance'] = [getDistance(lat_station, lon_station, lat, lon) 
							for (lat_station,lon_station) 
							in zip(stations['Longitude (Decimal Degrees)'], stations['Latitude (Decimal Degrees)'])]
	closest_station = stations[stations.Distance == stations.Distance.min()]
	return closest_station['Station ID']

#for a given address string
def getLatLon(address_str, city=""):
	geolocator = geopy.geocoders.Nominatim(user_agent="GoogleV3")
	location = geolocator.geocode(address_str)
	print(location.address)
	print((location.latitude, location.longitude))