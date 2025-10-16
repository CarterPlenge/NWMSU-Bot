# NWMSU's Discord bot
This is a Discord bot for Northwest esports' Discord server.

The purpose of this bot is to create automated features to aid the Northwest esports Discord server

The secondary purpose is to create a space where new computer science students can practice contributing to open-source projects. 

Or at least that's what this should be. It's not much right now.

## Current functionality

### Commands

#### Regular access
 - ```/about``` prints info about the bot
 - ```/gameRequest```requests a game to be added to the esports lab.
#### Boardmember access
 - ```/healthCheck``` make sure the database is connected
 - ```/say``` makes the bot say what you typed
#### admin access
 - ```/databaseQuery``` used to retrieve information from the database.
 - ```status``` change bots status.

## Contributing and updating

### What to contribute
 - Check PR (Pull requests) for issues/bugs/feature requests
 - If there are none, consider asking the esports organizer if they need anything
 - ask for approval to implement your own unique features, as they may not be welcome. (ie, a PR to send "hello world" every 5 seconds is not getting added.)

### Code formatting rules
Most open-source projects will only accept your PR if it meets their coding standards. However, this project doesn't have a lot of steam at the moment, so it will mostly be laissez-faire. Just use decent names and comments so others can read them. If you name all your variables after fictional characters, your PR might get denied, or maybe it won't. who knows.

### Getting started
#### Getting the project locally
software needed:
 - Docker           to run the bot and db
 - git              to clone from GitHub
Software recommended:
 - Python           if you want to run code outside of Docker
 - preferred IDE    if you don't want to edit everything in a text editor

Step 1: Clone the repo
Remember to cd to your desired directory 
```bash
git clone https://github.com/GameMagma/NWMSU-Bot.git
cd NWMSU-Bot
```

Optional Step: Creating a virtual environment
```bash
# if you want to run code locally, I would recommend using a venv
python -m venv env
pip install -r requirements.txt

# if psycopg2-binary==2.9.11 fails
# run "pip install psycopg2" instead
```

Step 2: Setting up .env
Use .envExample to create your .env
command to do so
```bash
cp .envExample .env
```

```
# You will need to create your own Discord bot, as sharing is a security risk
# You will also need a Discord server where you can test it out
DISCORD_TOKEN= # put your Discord bot's token here
GUILD_ID=   # put the guild_id of the server here


SQL_USER= testing        # create whatever username you want
SQL_PASSWORD= 1234       # create whatever password you want

SQL_HOST= postgres       # leave as is, match docker
SQL_PORT= 5432           # the port you want it to run on (5432 by default)
SQL_DATABASE= dbtest     # name it whatever you want          
```

Step 3: Starting containers
```bash
# make sure you have Docker running

# build the services
docker compose build

# start the containers
docker compose up -d # -d runs it detached 
```
use ```docker compose down``` to stop containers

You should have a working local clone of the project now

#### Project architectureA 
basic overview of where we put commands and what files do what. Check the actual directory for all files, as this is just a static overview and my be out of date. Check ```docs/``` for more information
```
commands/           # holds all commands
├── user/           # commands in here should be callable for all users
│   ├── gameRequest.py
│   ├── about.py
│   └── __init__.py # used to init commands in this folder
├── board/           # commands in here should be callable for board members
│   ├── healthCheck.py
│   ├── setStatus.py
│   └── __init__.py 
├── admin/           # commands in here should be callable for the select few
│   ├── shutdown.py
│   └── __init__.py 
docs/               # holds additional documentation

.dockerignore       # tells Docker what to ignore (not copy)
.envEXAMPLE         # .env creation reference
.gitignore          # tells git what to ignore
requirements.txt    # keeps all required external libraries needed to run this project

channel.py          # holds logic for locking commands to channels
clearCommands.py    # purges all commands; debugging script; will probably be removed
SQLManager          # holds logic for database operations
discordBot.py       # defines class discordBot, which interacts with Discord

docker-compose.yml  # tells Docker how to build the project
Dockerfile          # tells Docker how to build a container
init.sql            # initial template for database initialization

main.py
```

## TODO
 - write unit test or something
 - Error handling
