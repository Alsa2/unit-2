import requests
print("test")
login = {"username": "bob", "password": "B@bisthebestname"}

req = requests.post("http://192.168.6.142/login", json=login)
access_token = req.json()["access_token"]
print(access_token)


auth = {"Authorization": f"Bearer {access_token}"}

new_sensor ={ "type": "Temperature","location": "R2-10B", "name": "sensor_alex_bern_2","unit":"C",}

r = requests.post('http://192.168.6.142/sensor/new', json=new_sensor, headers=auth)
print(r.json())

