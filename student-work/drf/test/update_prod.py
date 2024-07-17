import requests
import json

url = "http://127.0.0.1:8000/products/2/"

payload = json.dumps({
  "name": "1234"
})
headers = {
  'Authorization': 'Token 73fd8d65a860b13df5d567cb5a736f6872894934',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
