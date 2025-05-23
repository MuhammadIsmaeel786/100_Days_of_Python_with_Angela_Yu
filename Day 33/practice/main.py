import requests
from datetime import datetime
MY_LAT = 33.6995086
MY_LNG = 73.0362897

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)



sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
