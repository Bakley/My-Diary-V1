import os
import psycopg2

from app import app
from app.config_database import config

from app.models.createdb import connect_to_db

class Database:
    """Contains helpers methods for connecting to the database"""

    def __init__(self):
        params = config()
        print("yes----", app.config)
        if app.config['TESTING']:
            params['database'] = "mydiaryentries_testing"

        connect_to_db()
        if 'DATABASE_URL' in os.environ:
            database_url = os.environ['DATABASE_URL']
            print(database_url)
            self.conn = psycopg2.connect(database_url)
        
        else:
            self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def insert(self, table, columns, values, returning=None):
        """
        Inserts elements into a table given columns and values
        Returns the values returned after executing the sql statement
        """
        columns = str(columns).replace("\'", "")
        values = str(values)
        sql = "INSERT INTO " + table + " " + columns + " VALUES " + values
        if returning:
            sql = sql + " RETURNING " + returning

        return_val = self.execute_sql(sql)
        return return_val

    def select(self, table, columns, left_join=None, where=None):
        """
        Selects elements in the database using the select statement
        """
        columns = str(columns).replace("\'", "")
        sql = "SELECT " + columns + " FROM " + table
        if left_join:
            sql = sql + " LEFT JOIN " + left_join
        if where:
            sql = sql + " WHERE " + where

        return_val = self.execute_sql(sql)
        return return_val

    def update(self, table, sett, where=None):
        sql = "UPDATE " + table + " SET " + sett
        if where:
            sql = sql + " WHERE " + where

        return_val = self.execute_sql(sql, fetch=False)
        return return_val

    def execute_sql(self, sql, fetch=True):
        """Executes the sql statement and returns the values from the database"""
        return_val = None
        try:
            self.cur.execute(sql)
            if fetch:
                return_val = self.cur.fetchall()
            else:
                return_val = ['Empty data']
            self.conn.commit()
            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: ", error)
        finally:
            if self.conn is not None:
                self.conn.close()

        return return_val