import requests

login = {"username": "bob", "password": "B@bisthebestname"}

req = requests.post("http://192.168.6.142/login", json=login)
access_token = req.json()["access_token"]
print(access_token)

auth = {"Authorization": "Bearer " + access_token}

req = requests.get("http://192.168.6.142/sensor/sensor_alex_bern_1", headers=auth)
print(req)