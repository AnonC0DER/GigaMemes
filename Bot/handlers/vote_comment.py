from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import *


@Client.on_message(filters.command('vote'))
async def Vote(client, message: Message):
    '''
    Vote fucntion for robot using GigaMemes REST APIs
    '''
    # Get username and password
    username = await client.ask(message.chat.id, 'Send your username')
    password = await client.ask(message.chat.id, 'Send your password')
        
    # Get token
    try:
        token = Get_JWT_for_bot(username.text, password.text)
    except:
        raise await client.send_message(message.chat.id,'Invalid username or password !')

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
    
        else:
            raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')

    else:
        await client.send_message(message.chat.id,'Wrong value !\n\nOnly up and down values are acceptable')



@Client.on_message(filters.command('comment'))
async def Vote(client, message: Message):
    '''
    comment fucntion for robot using GigaMemes REST APIs
    '''
    # Get username and password
    username = await client.ask(message.chat.id, 'Send your username')
    password = await client.ask(message.chat.id, 'Send your password')
        
    # Get token
    try:
        token = Get_JWT_for_bot(username.text, password.text)
    except:
        raise await client.send_message(message.chat.id,'Invalid username or password !')

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

    else:
        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')