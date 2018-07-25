import os
import psycopg2


from app.config import Config
from app.config_database import config

def connect_to_db():
    """Creates the database"""
    commands = (
        """
            CREATE TABLE users(
            id serial PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR NOT NULL
        )
        """
        """
            CREATE TABLE entries(
            id serial,
            user_id INTEGER NOT NULL,
            title VARCHAR NOT NULL,
            description VARCHAR NOT NULL,
            created_at timestamp NOT NULL,
            last_modified timestamp NOT NULL,
            PRIMARY KEY (user_id , id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        """
    )
    
    conn = None
    try:
        params = config()
    
        if Config['testing']:
            params['database'] = "mydiaryentries_testing"

        if 'DATABASE_URL' in os.environ:
            database_url = os.environ['DATABASE_URL']
            print(database_url)
            conn = psycopg2.connect(database_url)
        else:
            conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
