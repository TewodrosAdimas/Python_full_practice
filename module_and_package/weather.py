# import requests

# API_KEY = '79ff9471a6aab31dbb81d5aff5c183e1'
# CITY_NAME = input("Enter city name: ")
# # URL for the OpenWeatherMap API
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# def get_weather(api_key, city):
#     url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()
#         print(data)
#         # Extract relevant information
#         temperature = data['main']['temp']
#         weather_description = data['weather'][0]['description']
#         # Print out the weather information
#         print(f"City: {city}")
#         print(f"Temperature: {temperature}°C")
#         print(f"Weather: {weather_description}")
#     else:
#         # Print an error message if the request was not successful
#         print(f"Error fetching weather data: {response.status_code}")

# #if __name__ == "__main__":
# #get_weather(API_KEY, CITY_NAME)



# def fetch_html(url):
#     # Make the request to fetch HTML content
#     response = requests.get(url)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         html_content = response.text  # Get HTML content
#         print(html_content)  # Print or process HTML content
#     else:
#         print(f"Error fetching HTML: {response.status_code}")

# url = " "  # Replace with your desired URL
# #fetch_html(url)