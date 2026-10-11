import requests,os

BASE_URL = 'http://127.0.0.1:8120'

IS_LOGINED = False

def delete_post(post_id: int):
    try:
        uri = f'{BASE_URL}/deletepost'

        payload = {'id': post_id}
        response = requests.delete(uri, json=payload, timeout=5)

        return response.json()
    except:
        return f'Error {uri} failed to delete'

def create_post(post_name:str, post_id:int):
    try:
        uri = f'{BASE_URL}/newpost'
        payload = {
            'id' : post_id,
            'name' : post_name
        }

        create_post_response = requests.post(uri, json=payload, timeout=5)
        return create_post_response.json()

    except:
        return f'Error failed to create a post: {post_name}'

def get_all_posts():
    try:
        uri = f'{BASE_URL}/getposts'
        create_result = requests.get(uri)

        return create_result.json()
    except:
        return f'Error failed to create a event get posts'

def data_base_checker():
    path = r'instance\Database.db'

    if os.path.exists(path):
        return 200
    else:
        return 404

def check_for_elements():
    server_code_path = r'Server\Server_Core.py'
    templates_file = r'Server\templates'
    css_path = r'Server\templates\style.css'

    if os.path.exists(server_code_path):
        if os.path.exists(templates_file) and os.path.exists(css_path):
            return 200
        else:
            return 404
    else:
        return 404

def login(password):
    uri = f'{BASE_URL}/admin'

    payload = {'password': password}

    request = requests.post(uri, json=payload)
    answer = request.json()

    if answer == 'Admin':
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        result_s = data_base_checker()
        if result_s == 404:
            print('File: Database.db not found, run Server_core.py file')
            break

        result_s = check_for_elements()
        if result_s == 404:
            print('Element not fount...')
            break

        print('|--------------------------------------------------------------------|')
        chooser = int(input('Create post-1,Delete post-2,Get all posts-3,End Programm-4: '))
        if chooser == 1:
            name = str(input('Enter your post name: '))
            id = int(input('Enter your post id: '))

            result = create_post(name, id)
            print(f'result output: {result}')
        elif chooser == 2:
            id = int(input('Enter your post id to delete: '))
            result = delete_post(id)
            print(f'result output: {result}')
        elif chooser == 3:
            result = get_all_posts()
            print(f'result output: {result}')
        # elif chooser == 4:
        #     id = int(input('Enter password to get admin perms: '))
        #     IS_LOGINED = login(id)
        elif chooser == 4:
            print('|--------------------------------------------------------------------|')
            print('Stopping the CLIENT programm,Server is still active')
            print('|--------------------------------------------------------------------|')
            break
        else:
            print(f'Invalid number: {chooser} please try again.')