from requests import get, post
# Don't forget to run the project by : python manage.py runserver
#############################

# To prevent any weird errors, put a slash in the end of the every URL

# Replace it with your own ip address or domain address or 
# if you are running the project on local machine leave it alone.
BASE_URL = 'http://127.0.0.1:8000/'


# Register
def Register():
    '''Example of registration using GigaMemes rest api'''
    URL = BASE_URL + 'api/users/register/'
    
    # input data
    data = {
        'email' : 'test@gamil.com',
        'username' : 'testuser',
        'password' : 'testpass',
        'password2' : 'testpass'
    }

    # create post request
    request = post(url=URL, data=data)
    print(request)



# Get JWT authentication token
def Get_JWT():
    '''Example of how to get JWT using GigaMemes rest api'''
    URL = BASE_URL + 'api/users/token/'

    # input data
    data = {
        'username' : 'testuser',
        'password' : 'testpass'
    }

    # create post request
    request = post(url=URL, data=data)
    print(request.text)



# Create new meme
def Create_meme():
    '''Example of how to create new meme using GigaMemes rest api'''
    URL = BASE_URL + 'api/create-meme/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # input file (Meme image)
    files = {'image': open('PUT IMAGE PATH HERE', 'rb')}

    # input data
    data = {
        'title' : 'Test',
        'text' : 'Test text',
        'tags' : [
            'tag_1_id',
            'tag_2_id',
        ]
    }

    # create post request
    request = post(URL, headers=headers, data=data, files=files)
    print(request)



# Create new tag
def Create_tag():
    '''Example of how to create new tag using GigaMemes rest api'''
    URL = BASE_URL + 'api/create-tag/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # input data
    data = {
        'name' : 'tag_name',
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    print(request)



# Search memes
def Search_meme():
    '''Example of how to search meme using GigaMemes rest api'''
    URL = BASE_URL + 'api/search-meme/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # input data
    data = {
        'query' : 'test search value',
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    print(request.text)



# Vote meme
def Vote_meme():
    '''Example of how to vote meme using GigaMemes rest api'''
    URL = BASE_URL + 'api/vote-meme/PUT MEME ID HERE/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # input data
    data = {
        'vote' : 'up',
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    print(request)


# Comment meme
def Comment_meme():
    '''Example of how to comment meme using GigaMemes rest api'''
    URL = BASE_URL + 'api/comment-meme/PUT MEME ID HERE/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # input data
    data = {
        'body' : 'Great',
    }

    # create post request
    request = post(URL, headers=headers, data=data)
    print(request)



# Get single meme
def Get_meme():
    '''Example of how to get single meme using GigaMemes rest api'''
    URL = BASE_URL + 'api/single-meme/PUT MEME ID HERE/'

    # input headers (authentication token)
    headers = {
	'Authorization' : 'Bearer PUT JWT(access) TOKEN HERE'
    }

    # create post request
    request = get(URL, headers=headers)
    print(request.text)


# Get all memes
def Get_memes():
    '''Example of how to get all memes using GigaMemes rest api'''
    URL = BASE_URL + 'api/memes/'

    # create post request
    request = get(URL)
    print(request.text)