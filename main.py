import requests

api_key ="c0c1def321c29671105acd9d609a8438"

user_input = input("enter your city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)

if weather_data.status_code == 200:
    print("✅ Success! API Response:")
    print(weather_data.json())  # पूरा JSON Response प्रिंट करें
elif weather_data.status_code == 404:
    print("❌ Error 404: City not found. Please check the spelling.")
else:
    print(f"⚠️ Error {weather_data.status_code}: API request failed. Try again later.")
    
print(weather_data.status_code)