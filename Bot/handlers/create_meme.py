from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.functions import Create_meme_from_bot, Get_JWT_for_bot
from asyncio import sleep
from os import remove


''''
This file is just made for getting memes with information from user and send it to be posted on the website
'''


@Client.on_message(filters.command('create_meme'))
async def sendmeme(client, message: Message):
    username = await client.ask(message.chat.id , 'Send Your Username') # Asks for Username to get token
    while not username.text: # if user's message didn't have text, bot will ask for a username again
        username = await client.ask(message.chat.id,"I said send your **Username**") # Asks for username again
    
    passwd = await client.ask(message.chat.id , 'Send Your Password') # Asks for password to get token
    while not passwd.text: # if user's message didn't have text, bot will ask for a password again
        passwd = await client.ask(message.chat.id,"I said send your **Password**") # Asks for password again
    
    try:
        token = Get_JWT_for_bot(username.text, passwd.text) # this gets access token using username and password that user provided

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
        await passwd.reply("Invalid username or password !")

