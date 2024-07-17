import requests
import json

url = "http://127.0.0.1:8000/products/2/"

# * удаление товара по артикулу
payload = ""
headers = {
  'Authorization': 'Token 73fd8d65a860b13df5d567cb5a736f6872894934',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

# * Множественное удаление товаров
url = "http://127.0.0.1:8000/products/multiple_delete/"

payload = json.dumps([
  "2", "3"
])

headers = {
  'Authorization': 'Token 16bf6611b0b9e96ea5ae9f45a576ee9a4c8d1762',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
