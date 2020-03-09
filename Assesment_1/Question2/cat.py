import requests

def cat_facts(number):
    response = requests.get(f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={number}')
    if response.status_code != 200:
        raise ConnectionError
    data = response.json()
    for i in data:
        print(i['text'])

cat_facts(4)