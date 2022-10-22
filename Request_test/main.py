from urllib import response
import requests

# Создаем питомца с именем Pretty и id 1555
data_newpet = {
  
  "id": 1555,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pretty",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response=requests.post("https://petstore.swagger.io/v2/pet", json = data_newpet)
print(response.text)

# Меняем питомцу с id 1555 имя на Lucky
data_changePet = {
  
  "id": 1555,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Lucky",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response=requests.put("https://petstore.swagger.io/v2/pet", json = data_changePet)
print(response.text)

# Поиск питомца по id (например id=1555)
response=requests.get("https://petstore.swagger.io/v2/pet/1555")
print(response.text)