import requests 

r = requests.get("http://localhost:5000/health")
print(r.status_code)