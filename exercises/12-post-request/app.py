import requests

url = 'https://assets.breatheco.de/apis/fake/sample/post.php'

x = requests.post(url)

print(x.text)