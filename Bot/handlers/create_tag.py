from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import *
######################################


@Client.on_message(filters.command('create_tag'))
async def CreateTag(client, message: Message):
    '''
    Create Tag fucntion for robot using GigaMemes REST APIs
    '''
    # Get username and password
    username = await client.ask(message.chat.id, 'Send your username')
    password = await client.ask(message.chat.id, 'Send your password')
        
    # Get token
    try:
        token = Get_JWT_for_bot(username.text, password.text)
    except:
        raise await client.send_message(message.chat.id,'Invalid username or password !')

    # Get tag name
    tag_name = await client.ask(message.chat.id, 'Send your tag name')
    
    confirmation = await client.ask(message.chat.id, f'Okay, your tag name is {tag_name.text}.\n\nMax length = 200\nDo you want me to create this tag? (yes/no)')
    if confirmation.text.lower() == 'yes':
        # create post request
        req = Create_tag(token, tag_name.text)
        # check response
        if 'id' in req:
            await client.send_message(message.chat.id, f'Done !\n\nYour tag name : {tag_name.text}')
            
        else:
            raise await client.send_message(message.chat.id, req)


    else:
        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

    