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
  'Authorization': 'Token 73fd8d65a860b13df5d567cb5a736f6872894934',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=RvuTj0SrOxgBFbVhzx71b3ZKjjir4EMp'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# # * Добавление нескольких товаров
# payload = json.dumps([
#   {
#     "articule": "4",
#     "name": "2",
#     "description": "1",
#     "price": 123,
#     "shop":"1"
#   },
#   {
#     "articule": "3",
#     "name": "2",
#     "description": "1",
#     "price": 123,
#     "shop":"1"
# #   }
# # ])
#
#
# response = requests1.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
