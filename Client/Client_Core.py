import requests

BASE_URL = 'http://127.0.0.1:8120'

def delete_post(post_id: int):
    uri = f'{BASE_URL}/deletepost'

    payload = {'id': post_id}
    response = requests.delete(uri, json=payload, timeout=5)

    return response.json()

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
        return f'Error failed to create a post'

def get_all_posts():
    try:
        uri = f'{BASE_URL}/getposts'
        create_result = requests.get(uri)

        return create_result.json()
    except:
        return f'Error failed to create a event get posts'

if __name__ == "__main__":
    while True:
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
        elif chooser == 4:
            print('|--------------------------------------------------------------------|')
            print('Stopping the programm')
            print('|--------------------------------------------------------------------|')
            break
        else:
            print(f'Invalid number: {chooser} please try again.')