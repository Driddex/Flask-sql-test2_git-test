import json, requests

BASE_URI = 'http://127.0.0.1:8000'

def Create_user(name, id):
    create_url = f'{BASE_URI}/create'
    request_result = requests.post(create_url, json={'name': name, 'id': id})

    response = request_result.json()

    if response.get('status') == 'success':
        print(f'User with name: {name} and {id} id has been created...')
    else:
        print(f'Failed to create user...')

Create_user('Dridex', 4)