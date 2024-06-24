import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

data = response.json() 


def get_titles(x):
    titles= []
    posts = x['posts']
    for post in posts:
        titles = post['title'].append()

    return titles


print(get_titles(data))