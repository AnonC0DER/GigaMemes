from tkinter.tix import CheckList
from webbrowser import get
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import *
from handlers.database import *
######################################

def Checker(id):
    '''
    Check token and if the token didn't work it will return token_not_valid.
    Else it will return user token
    '''
    Get_token = Get_token_from_db(id)
    req = Check_JWT(Get_token)

    print(Get_token, req)
    if 'True' in req:
        token = Get_token
        return token

    else:
        token = req
        return token



@Client.on_message(filters.command('create_tag'))
async def CreateTag(client, message: Message):
    '''
    Create Tag fucntion for robot using GigaMemes REST APIs
    '''
    token = Checker(message.chat.id)
    # if token wasn't valid, it'll ask for username and password again
    if token == 'token_not_valid':
        # if the token has expired or it wasn't in database, it will ask for username and password
        username = await client.ask(message.chat.id, 'Send your username')
        password = await client.ask(message.chat.id, 'Send your password')
            
        # Get token
        try:
            token = Get_JWT_for_bot(username.text, password.text)
        except:
            raise await client.send_message(message.chat.id,'Invalid username or password !\n\nIf you need to create a new account send /register for me.')
    
    else:
        pass

    # Get tag name
    tag_name = await client.ask(message.chat.id, 'Send your tag name')
    # Confirm to create tag
    confirmation = await client.ask(message.chat.id, f'Okay, your tag name is {tag_name.text}.\n\nMax length = 200\nDo you want me to create this tag? (yes/no)')
    if confirmation.text.lower() == 'yes':
        # create post request
        create_tag_req = Create_tag(token, tag_name.text)
        # check response
        if 'id' in create_tag_req:
            await client.send_message(message.chat.id, f'Done !\n\nYour tag name : {tag_name.text}')
            
            # Get token from database, then check the token. If the token works fine, continue else it will save the token in database
            Get_token = Get_token_from_db(message.chat.id)
            result = Check_JWT(Get_token)
            if result != 'True':
                # Save user_id and user_token in database
                save_token = await client.ask(message.chat.id, "Do you want me to save your token, so you don't need to login again for next 24h? (yes/no)")
                if save_token.text.lower() == 'yes':
                    # First check the user chat ID, If the user is already exists then it updates the existing UserID token Else it adds new UserID and new UserToken to database
                    get_token = Get_token_from_db(save_token.chat.id)
                    result = Check_JWT(get_token)
                    if result != 'True':
                        if get_token == None:
                            Add_new_token(save_token.chat.id, token)

                        else:
                            Update_token(save_token.chat.id, token)
                    
                    await client.send_message(message.chat.id, 'Done !\nYour token has saved.')
                
                else:
                    raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

        else:
            raise await client.send_message(message.chat.id, 'Somthing went wrong !')
        

    else:
        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

    