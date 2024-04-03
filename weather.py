import requests
from geopy.geocoders import Nominatim
import datetime
import pandas as pd
class API:

    def run(self,city):
        if len(city)>0:
            city=city
        else:
            city='Yamuna Nagar, Haryana'
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        geolocator = Nominatim(user_agent="forecast")
        location = geolocator.geocode(city)
        print(location)
        cordinates=[location.latitude,location.longitude]
        querystring = {"q":cordinates}

        headers = {
            "X-RapidAPI-Key": "013070968bmshfd2f3199ff22b00p1204cbjsn9904c1e66207",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        data=response
        print(response)
        print(type(response))
        print(type(data))
        # print(datetime.datetime())
        url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

        querystring = {"q":city}

        headers = {
            "X-RapidAPI-Key": "013070968bmshfd2f3199ff22b00p1204cbjsn9904c1e66207",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response2 = requests.get(url, headers=headers, params=querystring)
        data2=response2.json()
        print(data2)
        current_time = datetime.datetime.now()
        
        
        df = pd.DataFrame(data)
        print(df)
        
        payload={
            'day':current_time.strftime('%A'),
            'date':current_time.date,
            'city':data['location']['name'],
            'temp':data['current']['temp_c'],
            'tempf':data['current']['temp_f'],
            'sky':data['current']['condition']['text'],
            'desc':data['current']['condition']['text'],
            'wind':data['current']['wind_kph'],
            'winddir':data['current']['wind_dir'],
            'priciption':data['current']['precip_mm'],
            'humidity':data['current']['humidity'],
            'uv':data['current']['uv'],
            'last_upd':data['current']['last_updated'],
            'cloud':data['current']['cloud'],
            'vis':data['current']['vis_km'],
            'FEELSLIKE':data['current']['feelslike_c'],
            'pre':data['current']['pressure_mb'],
            'gust':data['current']['gust_kph'],
            'moonrise':data2['astronomy']['astro']['moonrise'],
            'moonset':data2['astronomy']['astro']['moonset'],
            'moonlumi':data2['astronomy']['astro']['moon_illumination'],
            'moonphase':data2['astronomy']['astro']['moon_phase'],
        }
        return payload;
