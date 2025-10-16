# The Database
## Where is it?
The database is stored in the named Docker volume ```postgres_data```.
This volume persists across container restarts and prevents re-running init.sql

init.sql is mounted into the Docker volume on its first creation to create the database

To remove the volume (and delete the database) use ```docker-compose down -v```.

## how to create a new table
### Add it to init.sql
This will cause the table to be created when the container is built for the first time
This will make it easier for people to build the database locally and work on this project

### Adding it to the built database
Since init.sql is only run when a container is created for the first time, we will have 
to manually create new tables.

First, we have to connect to the DB
```docker-compose exec postgres psql -U botuser -d discord_bot```

Then we create the table manually
```SQL
CREATE TABLE IF NOT EXISTS game_request (
    id SERIAL PRIMARY KEY,
    username BIGINT NOT NULL,
    game VARCHAR(255) NOT NULL,
    platform VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'pending'
);
```
