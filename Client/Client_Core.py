import json, requests, sys ,os

BASE_URI = 'http://127.0.0.1:8000'

def Create_user(name, id):
    create_url = f'{BASE_URI}/create'
    request_result = requests.post(create_url, json={'name': name, 'id': id})

    response = request_result.json()

    if response.get('status') == 'success':
        print(f'User with name: {name} and {id} id has been created...')
    else:
        print(f'Failed to create user...')


def Is_Files_Exists():
    path1 = r'Server\Database\SQLconsole.sql'
    path2 = r'Server\Server_Core.py'

    if os.path.exists(path2):
        if os.path.exists(path1):
            return True
        else:
            return False
    else:
        return False

print('---------------------------------------------')
print(f'Starting _SHIT_ programm')

while True:
    checker = Is_Files_Exists()
    if checker == False: print('Programm file not found'),sys.exit()

    print('---------------------------------------------')

    chooser_s = int(input('1-Create User,2-Delete User,3-End the Programm: '))

    if chooser_s == 1:
        name = input('Enter a name: ')
        id = int(input('Enter a id: '))

        Create_user(name,id)
    elif chooser_s == 2:
        print('gg')
    elif chooser_s == 3:
        print('Stopping the programm')
        print('---------------------------------------------')
        sys.exit()
    else:
        print('wrong answer....')