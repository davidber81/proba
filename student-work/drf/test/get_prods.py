import requests


# Получить все товары
url = "http://127.0.0.1:8000/products"


# Получить конкретный товар
url = "http://127.0.0.1:8000/products/2"

payload = {}
headers = {
  'Authorization': 'Token 73fd8d65a860b13df5d567cb5a736f6872894934',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
