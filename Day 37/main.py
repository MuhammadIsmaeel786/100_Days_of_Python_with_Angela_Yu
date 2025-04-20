import requests
from datetime import datetime
USERNAME = "username"
TOKEN = "your token here"
pixela_endpoint= "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"commit",
    "type":"int",
    "color":"shibafu"
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"

today = datetime(year=2025, month=4, day=19)

post_pixel_params = {
    "date":today.strftime('%Y%m%d'),
    "quantity":"7"
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel_params = {
    "quantity":"9"
}
# response = requests.put(url=update_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)