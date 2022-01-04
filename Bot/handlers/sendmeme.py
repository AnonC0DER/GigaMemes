from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from driver.decorators import sudo_filter
from config import LOG_CHANNEL
from asyncio import sleep
from os import remove

@Client.on_message(filters.command('sendmeme'))
@sudo_filter
async def sendmeme(client, message: Message):
    # Asks for image
    image = await client.ask(message.chat.id,"Ok, Send Your image")
    while not image.photo:
        image = await client.ask(message.chat.id,"I said send your **image**")
    # Asks for title
    title = await client.ask(message.chat.id,"Ok, Send Your title")
    while not title.text:
        title = await client.ask(message.chat.id,"I said send your **title**")
    # Asks for text
    text = await client.ask(message.chat.id,"Ok, Send Your text")
    while not text.text:
        text = await client.ask(message.chat.id,"I said send your **text**")
    # Asks for tags
    tags = await client.ask(message.chat.id,"Ok, Send Your tags")
    while not tags.text:
        tags = await client.ask(message.chat.id,"I said send your **tags**")
    # Asks for sender name
    sender = await client.ask(message.chat.id,"Ok, Send Your name")
    while not sender.text:
        sender = await client.ask(message.chat.id,"I said send your **name**")
    # Confirmation
    x = await message.reply_photo(f"{image.photo.file_id}" , caption=f"Title: {title.text}\nText: {text.text}\nTags: {tags.text}\nSender: {sender.text}\nAre you sure you want to send this shit?")
    kos = await client.listen(message.chat.id) # for getting yes or no answer
    await x.forward(LOG_CHANNEL) # forwards the meme with all information to the log channel
    if kos.text.lower() in ['yes' , 'اره' , 'yeah' , 'آره']:
        await image.download(f'{image.photo.file_id}.jpg')
        await kos.reply(f"It will be there in a second :)")
        await sleep(900)# Sleeps for 15 minutes then deletes the downloaded file
        try:
            remove(f'downloads/{image.photo.file_id}.jpg')
        except Exception as e:
            print(e)
    else:
        await kos.reply("Ok sir\nI don't send it")