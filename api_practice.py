import requests

url = 'https://dummyjson.com/products/1'
response = requests.get(url, verify=False)

data = response.json()
# data = data['id','title','category']
print(data)
