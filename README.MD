# NWMSU's Discord bot
This is a discord bot for Northwest esports' discord server.

The purpose of this bot is to create automated features to aid Northwest esport discord server

The secondary purpuose is to create a space where new computer science students can practice contriputing to opensource projects. 

or atleast thats what this should be. its not much right now.

## Current functionality

### Commands

#### Regular access
 - about: prints purpouse/functionality.
 - ping: server health check.
 - request: request a new game.
 - dbtest: database health check.
#### admin access
 - admin_close_connection: closes db connection.
 - admin_restart_connection: reset db connection.
 - admin_say: send a message using the bot account.
 - status_set: change bots status.
 - resync_commands: idk what this does.
 - shutdown: shuts the bot down.

## Contributing and updating

### What to contribute
 - Check PR (Pull requests) for issues/bugs/feature request
 - if there are none consider asking the esport organizers if they need anything
 - ask for aproval to impliment your own unique features as they may not be welcome. (ie: a PR to send "hello world" every 5 seconds is not getting added.)

### Code formating rules
most opensource projects will only accept your PR if it meets their coding standards. However this project doesnt have a lot of steam at the moment so it will mostly be laissez faire. Just use decent names and comments so others can read it. if you name all your variables after fictional characters your PR might get denied.

## TODO
 - write somthing so people can test localy. we cant be giving out the bots admin creditinals. 
 - write unit test or somthing
 - be better
 - SQL stuff
 - Error handling

 ## Project arcitectuer
basic overview of where we put commands. check actual directory for all files
```
commands/
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
main.py
discordBot.py
```

when adding a new command remember to update the init file in its dirctory.