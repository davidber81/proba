import requests
import json

url = "http://127.0.0.1:8000/products/"

# Множественное добавление
payload = json.dumps({
  "prodcuts": [
    {
      "name": "123243",
      "articule": "1243",
      "description": "asdgq",
      "price": 127
    },
    {
      "name": "1231223",
      "articule": "1223",
      "description": "asdgq",
      "price": 127
    },
    {
      "name": "1232223",
      "articule": "1231",
      "description": "asdgq",
      "price": 127
    }
  ]
})
# Одинарное добавление
# payload = json.dumps(
#     {
#       "name": "123243",
#       "articule": "1243",
#       "description": "asdgq",
#       "price": 127
#     },
# )


headers = {
  'Authorization': 'EpA4L9xGNQagAYKIyoiosA',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
