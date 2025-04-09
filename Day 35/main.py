import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your Api"
account_sid = "Your Sid"
auth_token = "Your Token"

weather_params = {
"lon" :  73.130411,
"lat": 33.572535,
"cnt":4,
"appid":api_key
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
          from_="Virtual Num",
        to="Your Num",
        #Whatsapp
     # from_="whatsapp:+14155238886",
     body="Assalamualaikum, Cloudy Weather, Drive Safely wear helmet while Riding 🏍️",
        # to = "whatsapp:+923279842502",
    )
    print(message.status)
