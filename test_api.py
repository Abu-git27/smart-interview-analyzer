import requests

url = "http://127.0.0.1:5000/analyze"

data = {
    "text": "I am confident and I have good communication skills."
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())