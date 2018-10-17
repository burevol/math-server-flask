import json
import requests

#data = {'temperature':'24.3'}
#data_json = json.dumps(data)
#payload = {'json_payload': data_json,}
#r = requests.get('http://127.0.0.1:5000/math/api/v1.0/data')
#print(r.json())

#r = requests.get('http://127.0.0.1:5000/math/api/v1.0/data/2')
#print(r.json())

# data = {'data': 24.3}
# r = requests.post('http://127.0.0.1:5000/math/api/v1.0/data', json=data)
# print(r)

# update = {"data": 177}
# r = requests.put('http://127.0.0.1:5000/math/api/v1.0/data/1', json=update)
# print(r)

r = requests.delete('http://127.0.0.1:5000/math/api/v1.0/data/2')

r = requests.get('http://127.0.0.1:5000/math/api/v1.0/data')
print(r, r.json())