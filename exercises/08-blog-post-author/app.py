import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

data = response.json() 

post = data['posts']
author = post[0]['author']
name = author['name']
print(name)


