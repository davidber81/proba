import requests
import json

# Получение всех товаров
url = "http://127.0.0.1:8000/products"

# Получение товара по артикулу
url = "http://127.0.0.1:8000/products/2"

headers = {
  'Authorization': 'Token d4e19f525fe15e1984a81e9751a80239f2fa9794',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
