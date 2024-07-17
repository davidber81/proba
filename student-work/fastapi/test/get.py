import requests
import json

# Получение конкретного товара по артикулу 1243
url = "http://127.0.0.1:8000/products/1243"

# Получение всех товаров
# url = "http://127.0.0.1:8000/products/"

headers = {
  'Authorization': 'VSDehxjZYmN7rk5TpF37cg',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
