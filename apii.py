import requests

# # get me marr the dhenat
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)


# post me kriju
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId":1,"title":"Buy milk", "completed":False}
# response = requests.post(api_url,todo)
# print(response.json())
# print(response.status_code)



#put me bo update
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)
# print(response.json())

# todo = {"userId":1,"title":"Wash car","Completed":True}
# response = requests.put(api_url,json=todo)
# print(response.json())



#patch me bo update pjeserisht
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)
# print(response.json())
# todo = {'title':'taulant'}
# response = requests.patch(api_url,json=todo)
# print(response.json())



#delete 
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.delete(api_url)
# print(response.json())



# api_url = "https://api.example.com/cars"
# response = requests.get(api_url)
# print(response.json())




import requests
import json

api_key = 'ce346bce4309d39f0b21edfc08b79606'
city = 'New York'  # Replace with the desired city name

# Make a request to the API
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
data = json.loads(response.text)

# Extract relevant weather information from the response
temperature = data['main']['temp']
humidity = data['main']['humidity']
weather_description = data['weather'][0]['description']

# Print the weather information
print(f'Temperature: {temperature} K')
print(f'Humidity: {humidity}%')
print(f'Weather description: {weather_description}')
