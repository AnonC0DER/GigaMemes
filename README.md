# GigaMemes
## A meme website using Djagno and Django rest framework. <br>
Users can register and login. They can upload their memes to website. <br>
Vote and comment system work perfectly. <br>
There are two ways to post new meme, vote or comment. Users can simply use website and post their memes. <br>
They also can do the same things using telegram robot, which is connected to backend by REST APIs. <br>



# Plans 
- [ ] Automate posts from Reddit


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
- there are two ways to run the robot
- First one : Simply run -> python manage.py runrobot
- Second one : Copy Bot folder anywhere you want and simply run -> python bot.py






