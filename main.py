import requests
city_name = "Hyderabad"
api_key = "0ca0ce081605356f5e30738979ba0355"
url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print("weather type :",data['weather'][0]['description'])
    print("temparature",data['main']['temp'])
    print("maximum temerature:",data['main']['temp_max'])
    print("minimum temerature:",data['main']['temp_min'])