import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
print(data["results"])

question_data = data["results"]