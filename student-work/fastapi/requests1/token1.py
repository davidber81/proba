import requests
import json

url = "http://127.0.0.1:8000/auth/token/"

payload = json.dumps({
  "username": "1",
  "password": "1"
})
headers = {
  'Authorization': 'NT_pyCEI0wWgUCuOzP4G9g',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
