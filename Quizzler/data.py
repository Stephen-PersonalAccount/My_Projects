import requests

"""This gets the questions for the quiz from the open Trivia database using an API"""
parameters = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

