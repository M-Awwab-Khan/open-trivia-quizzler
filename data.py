import requests

params = {
    'amount': 10,
    'category': 18,
    'type': 'boolean'
}
response = requests.get('https://opentdb.com/api.php', params=params)
response.raise_for_status()

question_data = response.json()['results']