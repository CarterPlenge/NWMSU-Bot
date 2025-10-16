# NWMSU's Discord bot
This is a discord bot for Northwest esports' discord server.

The purpose of this bot is to create automated features to aid Northwest esport discord server

The secondary purpuose is to create a space where new computer science students can practice contriputing to opensource projects. 

or atleast thats what this should be. its not much right now.

## Current functionality

### Commands

#### Regular access
 - ```/about``` prints info about the bot
 - ```/gameRequest``` request a game to be added to the esport lab.
#### Boardmember access
 - ```/healthCheck``` make sure the database is connected
 - ```/say``` makes the bot say what you typed
#### admin access
 - ```/databaseQuery``` used to retrive infromation from the database.
 - ```status``` change bots status.

## Contributing and updating

### What to contribute
 - Check PR (Pull requests) for issues/bugs/feature request
 - if there are none consider asking the esport organizer if they need anything
 - ask for aproval to impliment your own unique features as they may not be welcome. (ie: a PR to send "hello world" every 5 seconds is not getting added.)

### Code formating rules
Most opensource projects will only accept your PR if it meets their coding standards. However this project doesnt have a lot of steam at the moment so it will mostly be laissez faire. Just use decent names and comments so others can read it. if you name all your variables after fictional characters your PR might get denied. or maybe it wont. who knows.

### Getting started
#### Getting the project locally
software needed:
 - docker           to run the bot and db
 - git              to clone from github
software recommended:
 - python           if you want to run code outside of docker
 - preferred IDE    if you dont want to edit everything in a text editor

Step 1: Clone the repo
remember to cd to your desired directory 
```
git clone https://github.com/GameMagma/NWMSU-Bot.git
cd NWMSU-Bot
```

Optional Step: creating a virtual enviroment
```
# if you want to run code localy i would recommend using a venv
python -m venv env
pip install -r requirements.txt

# if psycopg2-binary==2.9.11 fails
# run "pip install psycopg2" instead
```

Step 2: setting up .env
use .envExample to create your .env
command to do so
```cp .envExample .env```

```
# you will need to create your own discord bot as sharing is a security risk
# you will also need a discord server where you can test it out
DISCORD_TOKEN= # put your discord bots token here
GUILD_ID=   # put the guild_id of the server here


SQL_USER= testing        # create whatever username you want
SQL_PASSWORD= 1234       # create whatever password you want

SQL_HOST= postgres       # leave as is, match docker
SQL_PORT= 5432           # the port you want it to run on (5432 by default)
SQL_DATABASE= dbtest     # name it whatever you want          
```

Step 3: Starting containers
```
# make sure you have docker running

# build the services
docker compose build

# start the containers
docker compose up -d # -d runs it detached 
```
use ```docker compose down``` to stop containers

You should have a working local clone of the project now

#### Project arcitectuer
basic overview of where we put commands and what files do what. check actual directory for all files as this is just a static overview and my be out of date. Check ```docs/``` for more information
```
commands/           # holds all commands
├── user/           # commands in here should be callable for all users
│   ├── gameRequest.py
│   ├── about.py
│   └── __init__.py # used to init commands in this folder
├── board/           # commands in here should be callable for boad members
│   ├── healthCheck.py
│   ├── setStatus.py
│   └── __init__.py 
├── admin/           # commands in here should be callable for select few
│   ├── shutdown.py
│   └── __init__.py 
docs/               # holds additional documentation

.dockerignore       # tells docker what to ignore (not copy)
.envEXAMPLE         # .env creation reference
.gitignore          # tells git what to ignore
requirements.txt    # keeps all required external libraries needed to run this project

channel.py          # holds logic for locking commands to channels
clearCommands.py    # purges all commands; debugging script; will probably be removed
SQLManager          # holds logic for database operations
discordBot.py       # defines class discordBot which interacts with discord

docker-compose.yml  # tells docker how to build the project
Dockerfile          # tells docker how to build a container
init.sql            # inital templet for database initialization

main.py
```

## TODO
 - write unit test or somthing
 - Error handling
