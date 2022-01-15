from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import Create_meme_from_bot, Get_JWT_for_bot, Check_JWT
from asyncio import sleep
from handlers import database
from os import remove
####################################################

def Checker(id):
    '''
    Check token and if the token didn't work it will return token_not_valid.
    Else it will return user token
    '''
    Get_token = database.Get_token_from_db(id)
    req = Check_JWT(Get_token)

    print(Get_token, req)
    if 'True' in req:
        token = Get_token
        return token

    else:
        token = req
        return token




@Client.on_message(filters.command('create_meme'))
async def sendmeme(client, message: Message):
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
    
    try:
        image = await client.ask(message.chat.id,"Ok, Send Your image") # Asks for image
        while not image.photo: # if user's message didn't have image, bot will ask for an image again
            image = await client.ask(message.chat.id,"I said send your **image**") # Asks for image again
        
        title = await client.ask(message.chat.id,"Ok, Send Your title") # Asks for title
        while not title.text: # if user's message didn't have text, bot will ask for a title again
            title = await client.ask(message.chat.id,"I said send your **title**") # Asks for title again
        
        text = await client.ask(message.chat.id,"Ok, Send Your text") # Asks for text
        while not text.text: # if user's message didn't have text, bot will ask for a text again
            text = await client.ask(message.chat.id,"I said send your **text**") # Asks for text again
        
        tags = await client.ask(message.chat.id,"Ok, Send Your tags IDs (only IDs)") # Asks for tags
        while not tags.text: # if user's message didn't have text, bot will ask for a tag again
            tags = await client.ask(message.chat.id,"I said send your **tags**") # Asks for tags again
        
        sender = await client.ask(message.chat.id,"Ok, Send Your name") # Asks for sender name
        while not sender.text: # if user's message didn't have text, bot will ask for his name again
            sender = await client.ask(message.chat.id,"I said send your **name**") # Asks for sender name again
        
        # Ask the user for confirming the Meme to send to website
        meme = await message.reply_photo(f"{image.photo.file_id}" , caption=f"Title: {title.text}\nText: {text.text}\nTags: {tags.text}\nSender: {sender.text}\nAre you sure you want to send this shit? Yes or No :)")
        confirmation = await client.listen(message.chat.id) # Used to get user answer
        # await meme.forward('-1001702073113') # forwards the meme with all information to the log channel
        
        if confirmation.text.lower() in ['yes' , 'yeah']: # if user says yes, meme will be approved
            await image.download(f'memes/{image.photo.file_unique_id}.jpg') # save the meme image to 'memes' folder using its file_id
            try:
                Create_meme_from_bot(title.text, text.text, tags.text, f'memes/{image.photo.file_unique_id}.jpg', token) #Tries to post the meme on the website
                await confirmation.reply(f"I just posted your lovely meme :)") 

                # Get token from database, then check the token. If the token works fine, continue else it will save the token in database
                Get_token = database.Get_token_from_db(message.chat.id)
                result = Check_JWT(Get_token)
                if result != 'True':
                    # Save user_id and user_token in database
                    save_token = await client.ask(message.chat.id, "Do you want me to save your token, so you don't need to login again for next 24h? (yes/no)")
                    if save_token.text.lower() == 'yes':
                        # First check the user chat ID, If the user is already exists then it updates the existing UserID token Else it adds new UserID and new UserToken to database
                        get_token = database.Get_token_from_db(save_token.chat.id)
                        result = Check_JWT(get_token)
                        if result != 'True':
                            if get_token == None:
                                database.Add_new_token(save_token.chat.id, token)

                            else:
                                database.Update_token(save_token.chat.id, token)
                        
                        await client.send_message(message.chat.id, 'Done !\nYour token has saved.')
                    
                    else:
                        raise await client.send_message(message.chat.id,'Okay.\n\nSend /help to get commands list')
            
            except Exception as e:
                await confirmation.reply(f'ErroR:\n{e}') # if it get's any error during posting the meme this line will send the error to sender
            await sleep(900)# Sleeps for 15 minutes then deletes the downloaded file
            try:
                remove(f'memes/{image.photo.file_unique_id}.jpg') # remove downloaded image
            except Exception as e: # if theres any errors in removing meme image it will print it
                print(e)
        
        else:
            await confirmation.reply("Ok sir\nI don't send it") # if user say anything except yes evereything will be cancelled

    except:
        await client.send_message(message.chat.id, "Invalid username or password !")

