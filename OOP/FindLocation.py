from geopy.geocoders import Nominatim

geoLocator  = Nominatim(user_agent="myothiha")
zipcode = input("Enter your zipcode : ")
location = geoLocator.geocode(zipcode,country_codes= "ES",language="en")
print(f"Zipcode : {zipcode}")
print("Details of zipcode is : {zipcode}",location)
