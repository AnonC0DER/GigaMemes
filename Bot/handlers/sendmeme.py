from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.decorators import sudo_filter
from config import LOG_CHANNEL
from asyncio import sleep
from os import remove

@Client.on_message(filters.command('sendmeme'))
@sudo_filter # filters sudo users
async def sendmeme(client, message: Message):
    image = await client.ask(message.chat.id,"Ok, Send Your image") # Asks for image
    while not image.photo: # if user's message didn't have image, bot will ask for an image again
        image = await client.ask(message.chat.id,"I said send your **image**") # Asks for image again
    title = await client.ask(message.chat.id,"Ok, Send Your title") # Asks for title
    while not title.text: # if user's message didn't have text, bot will ask for a title again
        title = await client.ask(message.chat.id,"I said send your **title**") # Asks for title again
    text = await client.ask(message.chat.id,"Ok, Send Your text") # Asks for text
    while not text.text: # if user's message didn't have text, bot will ask for a text again
        text = await client.ask(message.chat.id,"I said send your **text**") # Asks for text again
    tags = await client.ask(message.chat.id,"Ok, Send Your tags") # Asks for tags
    while not tags.text: # if user's message didn't have text, bot will ask for a tag again
        tags = await client.ask(message.chat.id,"I said send your **tags**") # Asks for tags again
    sender = await client.ask(message.chat.id,"Ok, Send Your name") # Asks for sender name
    while not sender.text: # if user's message didn't have text, bot will ask for his name again
        sender = await client.ask(message.chat.id,"I said send your **name**") # Asks for sender name again
    # Ask the user for confirming the Meme to send to website
    meme = await message.reply_photo(f"{image.photo.file_id}" , caption=f"Title: {title.text}\nText: {text.text}\nTags: {tags.text}\nSender: {sender.text}\nAre you sure you want to send this shit?")
    confirmation = await client.listen(message.chat.id) # Used to get user answer
    await meme.forward(LOG_CHANNEL) # forwards the meme with all information to the log channel
    if confirmation.text.lower() in ['yes' , 'اره' , 'yeah' , 'آره' , 'بله' , 'بلی']: # if user say yes, meme will be approved
        await image.download(f'memes/{image.photo.file_id}.jpg') # save the meme image to 'memes' folder using its file_id
        await confirmation.reply(f"It will be there in a second :)") 
        await sleep(900)# Sleeps for 15 minutes then deletes the downloaded file
        try:
            remove(f'memes/{image.photo.file_id}.jpg') # remove downloaded image
        except Exception as e: # if theres any errors in removing meme image it will print it
            print(e)
    else:
        await confirmation.reply("Ok sir\nI don't send it") # if user say anything except yes evereything will be cancelled