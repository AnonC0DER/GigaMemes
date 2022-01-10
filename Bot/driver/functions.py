from requests import post
import json

# To prevent any weird errors, put a slash in the end of the every URL

# Replace it with your own ip address or domain address or 
# if you are running the project on local machine leave it alone.
BASE_URL = 'http://127.0.0.1:8000/'

def Create_meme_from_bot(title, text, tags, image, token):
    URL = BASE_URL + 'api/create-meme/'

    # input headers (authentication token)
    headers = {
	'Authorization' : {token}
    }

    # input file (Meme image)
    files = {'image': open(image, 'rb')}

    # input data
    data = {
        'title' : {title},
        'text' : {text},
        'tags' : tags.split()
    }

    # create post request
    request = post(URL, headers=headers, data=data, files=files)
    print(request)

# Get JWT authentication token
def Get_JWT_for_bot(username, passwd):
    
    URL = BASE_URL + 'api/users/token/'

    # input data
    data = {
        'username' : {username},
        'password' : {passwd}
    }

    # create post request
    request = post(url=URL, data=data).text
    TOKEN = json.loads(request)['access']
    
    return TOKEN