import requests

dict = {
    "id": 2323,
    "title": "Very big project"
}

headers = {
    "Content-Type": "application/json"
}


response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=dict, headers=headers)
print(response.text)