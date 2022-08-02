import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 49, "name": "Tim", "views": 19995},
        {"likes": 20, "name": "Cris", "views": 1235787},
        {"likes": 77, "name": "Gomes", "views": 123551}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
