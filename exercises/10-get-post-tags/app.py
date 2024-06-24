import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

data = response.json() 

id_post = 146

def get_post_tags(x):
    posts = x['posts']
    for post in posts:
        if id_post == post['id']:
            return post['tags']

    return None


print(get_post_tags(data))