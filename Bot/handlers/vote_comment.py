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


@Client.on_message(filters.command('vote'))
async def Vote(client, message: Message):
    '''
    Vote fucntion for robot using GigaMemes REST APIs
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
   

    # Get meme ID
    meme_id = await client.ask(message.chat.id, 'Please send your meme ID')
    # Get vote value
    vote_value = await client.ask(message.chat.id, "What's your vote for this meme?\n\nup or down?")

    # Check value
    if vote_value.text.lower() == 'up' or vote_value.text.lower() == 'down':
        confirmation = await client.ask(message.chat.id, f'Okay, your vote value is {vote_value.text}.\nDo you want me to post this vote? (yes/no)')
        if confirmation.text.lower() == 'yes':
            # create post request
            req = Vote_meme(meme_id.text, vote_value.text, token)
            # check response
            if 'already' in req:
                # Send AlreadyError description
                raise await client.send_message(message.chat.id, json.loads(req)['AlreadyError'])

            await client.send_message(message.chat.id, f'Done !\n\nYour comment : {vote_value.text}')
            
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
            raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

    else:
        await client.send_message(message.chat.id,'Wrong value !\n\nOnly up and down values are acceptable')



@Client.on_message(filters.command('comment'))
async def Comment(client, message: Message):
    '''
    comment fucntion for robot using GigaMemes REST APIs
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

    # Get meme ID
    meme_id = await client.ask(message.chat.id, 'Please send your meme ID')
    # Get comment body 
    comment_body = await client.ask(message.chat.id, 'Write your comment :')

    # Check value
    
    confirmation = await client.ask(message.chat.id, f'Okay, your comment is \n\n"{comment_body.text}".\n\nDo you want me to post this comment? (yes/no)')
    if confirmation.text.lower() == 'yes':
        # create post request
        req = Comment_meme(meme_id.text, comment_body.text, token)
        await client.send_message(message.chat.id, f'Done !\n\nYour comment : {comment_body.text}')

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
        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')