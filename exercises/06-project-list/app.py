import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

data = response.json() 
project = data[1]['name']
print(project)


