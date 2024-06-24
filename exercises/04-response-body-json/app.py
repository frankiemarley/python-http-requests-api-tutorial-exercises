import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

data = response.json() 
print(f"Current time: {data['hours']} hrs {data['minutes']} min and {data['seconds']} sec")

# Current time: 17 hrs 35 min 38 sec