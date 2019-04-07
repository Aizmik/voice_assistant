import pandas as pd
import numpy as np
import psycopg2
import random


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS themes (
            theme_id SERIAL PRIMARY KEY,
            theme_keywords VARCHAR(255) NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS dialogs (
                parent_comment VARCHAR(255) NOT NULL,
                children_comment VARCHAR(255) NOT NULL,
                theme INTEGER,
                FOREIGN KEY(theme)
                REFERENCES themes(theme_id)
                )
        """,
       )
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=pikabu_comments user=neuralnet password=123")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print("closing connection")
            conn.close()


def insert_keyword(keywords):
    try:
        conn = psycopg2.connect("dbname=pikabu_comments user=neuralnet password=123")

        cur = conn.cursor()
        cur.execute("SELECT * FROM themes;")
        themes = cur.fetchall()

        for theme in themes:
            if theme[1] == keywords:
                cur.close()
                conn.close()
                return theme[0]

        cur.execute("INSERT INTO themes(theme_keywords) VALUES(%s) RETURNING theme_id;", (keywords,))
        theme_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return theme_id

def insert_phrase(parent, child, keyword):
    try:
        conn = psycopg2.connect("dbname=pikabu_comments user=neuralnet password=123")
        cur = conn.cursor()
        cur.execute("INSERT INTO dialogs(parent_comment, children_comment, theme) VALUES(%s,%s,%s)", (parent, child, keyword,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, parent, child)
    finally:
        conn.close()

def extract_to_txt(test_size = None):
    try:
        conn = psycopg2.connect("dbname=pikabu_comments user=neuralnet password=123")
        query = "SELECT parent_comment, children_comment FROM dialogs"
        data = pd.read_sql(query, conn)

        if(test_size):
            test = data.sample(test_size)
            np.savetxt(r'test_parent.txt', test['parent_comment'].values, fmt='%s',encoding='UTF-8')
            np.savetxt(r'test_children.txt', test['children_comment'].values, fmt='%s',encoding='UTF-8')

        np.savetxt(r'train_parent.txt', data['parent_comment'].values, fmt='%s',encoding='UTF-8')
        np.savetxt(r'train_children.txt', data['children_comment'].values, fmt='%s',encoding='UTF-8')

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()      



create_tables()