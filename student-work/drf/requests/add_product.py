import requests
import json

url = "http://127.0.0.1:8000/products/"

# * Добавление одного товара
payload = json.dumps([
    {
        "articule": "2",
        "name": "2",
        "description": "1",
        "price": 123,
        "shop":"1"
    }
])

headers = {
  'Authorization': 'Token 16bf6611b0b9e96ea5ae9f45a576ee9a4c8d1762',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# * Добавление нескольких товаров
payload = json.dumps([
  {
    "articule": "4",
    "name": "2",
    "description": "1",
    "price": 123,
    "shop":"1"
  },
  {
    "articule": "3",
    "name": "2",
    "description": "1",
    "price": 123,
    "shop":"1"
  }
])


response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
