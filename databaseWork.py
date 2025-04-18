import telebot
import sqlite3

def start(message):
    database = sqlite3.connect('users.db')
    dbCursor = database.cursor()
    dbCursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER                 
    )""")

    database.commit()

    people_id = message.chat.id
    dbCursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = dbCursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        dbCursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        database.commit()

def saveTheme(message):
    database = sqlite3.connect('users.db')
    dbCursor = database.cursor()
    dbCursor.execute("""CREATE TABLE IF NOT EXISTS themes(
	    name char,
	    user_id INTEGER
    )""")

    database.commit()

    theme = message.text
    user_id = message.chat.id
    dbCursor.execute(f"""INSERT INTO themes (name, user_id) VALUES("{theme}", {user_id})""")
    database.commit()

    #CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES login_id (id)