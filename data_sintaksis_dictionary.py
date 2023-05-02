user = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(user)
print(user["id"])
print(user["name"])
print(user["username"])
print(user["email"])
print(user["address"]["zipcode"])
print(user["address"]["geo"]["lng"])

print(user)
print(type(user))
print('\nUbah dictionary ke JSON')
import json
result = json.dumps(user)
print(result)
print(type(result))

with open('result.json', 'w') as file:
    json.dump(user, file)