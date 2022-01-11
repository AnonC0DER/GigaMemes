from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import *
######################################


@Client.on_message(filters.command('register'))
async def RegisterNewUser(client, message: Message):
    '''
    Register new user fucntion for robot using GigaMemes REST APIs
    '''
    # Get email, username, password and confirim password
    email = await client.ask(message.chat.id, 'Send your email')
    username = await client.ask(message.chat.id, 'Send your username')
    password = await client.ask(message.chat.id, 'Send your password')
    password2 = await client.ask(message.chat.id, 'Confirim your password')

    confirmation = await client.ask(message.chat.id, f'''
Okay, 
Your email address is {email.text}
Your username is {username.text}
Your password is {password.text}

Do you want me to create this account for you? (yes/no)
    ''')

    if confirmation.text.lower() == 'yes':
        # create post request
        req = Register(email.text, username.text, password.text, password2.text)
        print(req)
        # check response
        if 'email' in req:
            await client.send_message(message.chat.id, f'Done !\n\nYour email address : {email.text}\n\nYour username is : {username.text}')
            
        else:
            raise await client.send_message(message.chat.id, req)


    else:
        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

    