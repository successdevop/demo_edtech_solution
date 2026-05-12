from urllib import response

import requests

# joke_url = "https://official-joke-api.appspot.com/random_joke"
# response = requests.get(joke_url)
# response.raise_for_status()
# print(response.json())
# print(response.json()['punchline'])
# print(response.status_code)

# base_url = "https://api.sunrise-sunset.org/json"
#
# parameter = {
#     "lat": 6.621070,
#     "lng": 3.503440
# }
# response1 = requests.get(base_url, params= parameter)
# print(response1.json())

# api_key = "39bcbb6e9327fddc6db4a3d5a54fffb3"
# base_url = "https://api.openweathermap.org/data/2.5/weather"
#
# parameter = {
#     "lat": 6.621070,
#     "lon": 3.503440,
#     "appid": api_key
# }
# response1 = requests.get(base_url, params= parameter)
# print(response1.json())

# base_url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {
#     "title": 'sample testing',
#     "body": 'i am testing my post request',
#     "userId": 1,
# }
# response1 = requests.post(base_url, json=data)
#
# if response1.status_code == 201:
#     print("success")
#     print(response1.json())
# else:
#     print("fail")

base_url = "https://jsonplaceholder.typicode.com/posts/101"

data = {
    "id": 101,
    "title": 'learning flask',
    "body": 'Becoming a pro with flask',
    "userId": 1,
}
response1 = requests.put(base_url, json=data)
print(response1.status_code)

