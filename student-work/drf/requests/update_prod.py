import requests
import json

url = "http://127.0.0.1:8000/products/2/"

payload = json.dumps({
  "name": "1234"
})
headers = {
  'Authorization': 'Token 16bf6611b0b9e96ea5ae9f45a576ee9a4c8d1762',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
