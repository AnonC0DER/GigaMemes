from requests import post
import json

BASE_URL = 'https://gigamemes.pythonanywhere.com/'


def Create_meme_from_bot(title, text, tags, image, token):
    URL = BASE_URL + 'api/create-meme/'

    # input headers (authentication token)
    headers = {
	'Authorization' : f'Bearer {token}'
    }


    # input file (Meme image)
    files = {'image': open(image, 'rb')}

    # input data
    data = {
        'title' : title,
        'text' : text,
        'tags' : tags.split()
    }

    # create post request
    request = post(URL, headers=headers, data=data, files=files).text
    print(request)


# Vote meme
def Vote_meme(id, vote, token):
    URL = BASE_URL + f'api/vote-meme/{id}/'

    # input headers (authentication token)
    headers = {
	'Authorization' : f'Bearer {token}'
    }

    # input data
    data = {
        'vote' : vote,
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    return request.text
    

# Comment meme
def Comment_meme(id, body, token):
    URL = BASE_URL + f'api/comment-meme/{id}/'

    # input headers (authentication token)
    headers = {
	'Authorization' : f'Bearer {token}'
    }

    # input data
    data = {
        'body' : body,
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    return request.status_code


# Get JWT authentication token
def Get_JWT_for_bot(username, password):
    URL = BASE_URL + 'api/users/token/'

    # input data
    data = {
        'username' : username,
        'password' : password
    }

    # create post request
    request = post(url=URL, data=data).text
    TOKEN = json.loads(request)['access']
    
    return TOKEN


# Check JWT
def Check_JWT(token):
    URL = BASE_URL + 'api/check-jwt/'

    # input headers (authentication token)
    headers = {
	    'Authorization' : f'Bearer {token}'
    }

    # create post request
    request = post(url=URL, headers=headers).text
    try:
        response = json.loads(request)['code']
    except:
        response = json.loads(request)['IsAuthenticated']
    
    return response



# Create new tag
def Create_tag(token, tag):
    URL = BASE_URL + 'api/create-tag/'

    # input headers (authentication token)
    headers = {
	'Authorization' : f'Bearer {token}'
    }

    # input data
    data = {
        'name' : tag,
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    return request.text


# Register
def Register(email, username, password, password2):
    URL = BASE_URL + 'api/users/register/'
    
    # input data
    data = {
        'email' : email,
        'username' : username,
        'password' : password,
        'password2' : password2
    }

    # create post request
    request = post(url=URL, data=data)
    return request.text