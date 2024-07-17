import requests
import json
# Множественное удаление
url = "http://127.0.0.1:8000/products/"

payload = json.dumps([
  "1231",
  "124443"
])

# Одиночное удаление
# url = "http://127.0.0.1:8000/products/1223"

headers = {
  'Authorization': 'EpA4L9xGNQagAYKIyoiosA',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
