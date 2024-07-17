import requests
import json

url = "http://127.0.0.1:8000/shop/"

payload = json.dumps({
  "name": "12"
})
headers = {
  'Authorization': 'VSDehxjZYmN7rk5TpF37cg',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
