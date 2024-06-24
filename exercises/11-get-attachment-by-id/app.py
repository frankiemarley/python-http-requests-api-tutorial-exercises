import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

data = response.json() 

id_attachment = 137

def get_attachment_by_id(x):
    posts = x['posts']
    for post in posts:
        for attachment in post['attachments']:
           if attachment['id'] == id_attachment:
               return attachment['title']
    return None
               
    



print(get_attachment_by_id(data))