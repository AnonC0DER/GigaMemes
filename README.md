# GigaMemes
## A meme website using Djagno and Django rest framework. <br>
Users can register and login. They can upload their memes to the website. <br>
Vote and comment system work perfectly. <br>
There are two ways to post a new meme, vote or comment. Users can simply use the website and post their memes. <br>
They also can do the same things using telegram robot, which is connected to backend by REST APIs. <br>
[Live demo](http://gigamemes.pythonanywhere.com/api/)

[How this system works?](https://github.com/AnonC0DER/GigaMemes/blob/master/ProjectPreview/GigaMemes_preview.pdf)

**Give me a hand with front-end :)**
---

# Plans 
- [ ] Automate posts from Reddit
- [ ] Use a database in telegram robot

---

# How to run? 

## Backend
- git clone https://github.com/AnonC0DER/GigaMemes.git
- cd GigaMemes
- pip install -r requirements.txt
- use an online postgresql or local postgresql database or you can use sqlite3 (if you use postgresql don't forget to create .env file)
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


## Telegram robot
- create .env file (check config.py)
- Copy Bot folder wherever you want and simply run -> python bot.py

---
## Features
- Memes, Comment, Vote and Profile models 
- REST APIs :
1. Register
2. Authentication with JWT
3. Get all meme objects
4. Get single meme object
5. Create new meme
6. Create new tag
7. Vote & comment
8. Documentation 
- A telegram robot (using REST APIs)


---

# Files
- [Project preview (how everything works)](https://github.com/AnonC0DER/GigaMemes/tree/master/ProjectPreview)
- [Memes model, comments and vote](https://github.com/AnonC0DER/GigaMemes/tree/master/Memes)
- [Profile model](https://github.com/AnonC0DER/GigaMemes/tree/master/Users)
- [REST APIs](https://github.com/AnonC0DER/GigaMemes/tree/master/api)
- [Robot folder](https://github.com/AnonC0DER/GigaMemes/tree/master/Bot)
- [REST APIs example functions](https://github.com/AnonC0DER/GigaMemes/tree/master/api_examples_python)
- [Static files](https://github.com/AnonC0DER/GigaMemes/tree/master/static/)
