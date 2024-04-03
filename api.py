import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": "013070968bmshfd2f3199ff22b00p1204cbjsn9904c1e66207",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
# next 14 days 
import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"London","days":"3"}

headers = {
	"X-RapidAPI-Key": "013070968bmshfd2f3199ff22b00p1204cbjsn9904c1e66207",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
# print(response.json())
f=open('abc.txt','w+');
f.write(str(response.json()))
f.close

#sunrize sunsset
import requests

url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

querystring = {"q":"London"}

headers = {
	"X-RapidAPI-Key": "013070968bmshfd2f3199ff22b00p1204cbjsn9904c1e66207",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())